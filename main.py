from image_utils import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import ball
from PIL import Image

image = load_image(file_path)
clean_image = median(image, ball(4))
edgeMAG = edge_detection(clean_image)
#plt.hist(edgeMAG.flatten(), bins=256, range=(0, 255));
#plt.show()
edge_binary = edgeMAG <30
plt.imshow(edge_binary, cmap='gray')
edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
 
