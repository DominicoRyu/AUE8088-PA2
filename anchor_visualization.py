import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the anchors from the YAML file
anchors = {
    "P3/8": [16, 30],
    "P4/16": [62, 45],
    "P5/32": [156, 198]
}

# Define the image size and center
image_size = (640, 640)
center = (image_size[0] // 2, image_size[1] // 2)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.set_xlim(0, image_size[0])
ax.set_ylim(0, image_size[1])
ax.set_aspect('equal')
ax.invert_yaxis()

# Draw the anchors at the center of the image
for name, (w, h) in anchors.items():
    rect = patches.Rectangle((center[0] - w // 2, center[1] - h // 2), w, h, linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    ax.text(center[0] - w // 2, center[1] - h // 2, name, color='white', fontsize=12, bbox=dict(facecolor='red', alpha=0.5))

plt.tight_layout()
plt.savefig('anchors_plot.png')
plt.close()