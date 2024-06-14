import torch
from models.yolo import Model
from collections import OrderedDict

# Function to hook and print the output sizes of each layer
def print_layer_output_sizes(model, input_tensor):
    hooks = []

    def hook_fn(module, input, output):
        if isinstance(output, (list, tuple)):
            for out in output:
                if isinstance(out, torch.Tensor):
                    layer_info = {
                        "layer_name": module.__class__.__name__,
                        "output_shape": out.shape
                    }
                    layer_outputs.append(layer_info)
        else:
            layer_info = {
                "layer_name": module.__class__.__name__,
                "output_shape": output.shape
            }
            layer_outputs.append(layer_info)

    for name, module in model.named_modules():
        hooks.append(module.register_forward_hook(hook_fn))

    with torch.no_grad():
        model(input_tensor)

    for hook in hooks:
        hook.remove()

    return layer_outputs

# Load the trained YOLOv5 model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
checkpoint = torch.load('./runs/train/yolov5n/weights/best.pt', map_location=device)

# Create a model instance
model = Model(checkpoint['model'].yaml).to(device)

# Load the model weights
model.load_state_dict(checkpoint['model'].float().state_dict())

# Create an example input tensor
input_tensor = torch.rand(1, 3, 416, 416).to(device)

# Print layer output shapes
layer_outputs = []
layer_outputs = print_layer_output_sizes(model, input_tensor)

# Display the layer names and their output sizes
for layer in layer_outputs:
    print(f"Layer: {layer['layer_name']}, Output Shape: {layer['output_shape']}")
