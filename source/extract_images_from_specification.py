from spire.pdf.common import *
from spire.pdf import *

# Create a PdfDocument object
doc = PdfDocument()

# Load a PDF document
doc.LoadFromFile('output/TMF620/TMF620_Product_Catalog_userguide.pdf')

# Create a PdfImageHelper object
image_helper = PdfImageHelper()
image_count = 1
# Iterate through the pages in the document
for i in range(doc.Pages.Count):
    # Get the image information from the current page
    images_info = image_helper.GetImagesInfo(doc.Pages[i])
    # Get the images and save them as image files
    for j in range(len(images_info)):
        image_info = images_info[j]
        output_file = f"output/TMF620/images/image{image_count}.png"
        image_info.Image.Save(output_file)
        image_count += 1
doc.Close()
