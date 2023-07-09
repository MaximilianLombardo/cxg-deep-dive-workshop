#python screenshot_plus.py --width 3840 --height 2160 --crop-x 0 --crop-y 0 --crop-width 3840 --crop-height 2160 -o ~/Desktop/TestOutput.png "https://cellxgene.cziscience.com"

###Collection page ###
mkdir ../content/dataportal/images/collections

#Collection page - full screenshot
#python screenshot_plus.py --width 3200 --height 1800 -o ../content/dataportal/images/collections/fullscreen.png "https://cellxgene.cziscience.com/collections"
python screenshot_plus.py --width 1600 --height 900 -o ../content/dataportal/images/collections/fullscreen.png "https://cellxgene.cziscience.com/collections"

#Collection page

#Half screen
python image_crop.py ../content/dataportal/images/collections/fullscreen.png 0 0 3200 1500 ../content/dataportal/images/collections/halfscreen.png

#Header
python image_crop.py ../content/dataportal/images/collections/fullscreen.png 0 0 3200 96 ../content/dataportal/images/collections/header.png
python image_crop.py ../content/dataportal/images/collections/fullscreen.png 0 0 850 96 ../content/dataportal/images/collections/header_left.png
python image_crop.py ../content/dataportal/images/collections/fullscreen.png 5950 0 450 96 ../content/dataportal/images/collections/header_right.png

#Sample Collections - metadata
python image_crop.py ../content/dataportal/images/collections/fullscreen.png 500 133 2650 600 ../content/dataportal/images/collections/collections_metadata.png


### Collection Page: Tabula Sapiens ###

mkdir ../content/dataportal/images/TScollection

# Tabula Sapiens Collection Page Full Screenshot
# https://cellxgene.cziscience.com/collections/e5f58829-1a66-40b5-a624-9046778e74f5
python screenshot_plus.py --width 1600 --height 900 -o ../content/dataportal/images/TSCollection/fullscreen.png "https://cellxgene.cziscience.com/collections/e5f58829-1a66-40b5-a624-9046778e74f5"

#Abstract
python image_crop.py ../content/dataportal/images/TSCollection/fullscreen.png 0 120 1600 475 ../content/dataportal/images/TSCollection/abstract.png

#Contact
python image_crop.py ../content/dataportal/images/TSCollection/fullscreen.png 1600 120 1550 475 ../content/dataportal/images/TSCollection/contact.png

#Datasets
python image_crop.py ../content/dataportal/images/TSCollection/fullscreen.png 0 750 3200 525 ../content/dataportal/images/TSCollection/datasets.png




#### Datasets Page ### 


### Gene Expression ####

mkdir ../content/dataportal/images/geneexpression

#4-2_figure1.png

"images/CELLxGENE_gene_expression/breast.png"
#python image_crop.py ../content/geneExpression/images/CELLxGENE_gene_expression/breast.png 1400 1300 6000 650 ../content/geneExpression/images/geneExpressionBanner.png
python image_crop.py ../content/geneExpression/images/CELLxGENE_gene_expression/lung.png 1375 1300 5000 750 ../content/geneExpression/images/geneExpressionBanner.png


### Cell Guide ###
https://cellxgene.dev.single-cell.czi.technology/cell-guide/tissues/UBERON_0000948

#search
python screenshot_plus.py --width 1600 --height 900 -o ../content/cellguide/images/cellguideSearch.png "https://cellxgene.dev.single-cell.czi.technology/cell-guide/"
python image_crop.py ../content/cellguide/images/cellguideSearch.png 1050 500 1200 450 ../content/cellguide/images/cellguideSearchFocus.png


#tissue
python screenshot_plus.py --width 1600 --height 900 -o ../content/cellguide/images/cellguideHeart.png "https://cellxgene.dev.single-cell.czi.technology/cell-guide/tissues/UBERON_0000948"

#cell type - cardiac endothelial cell
python screenshot_plus.py --width 1600 --height 2000 -o ../content/cellguide/images/celltypelong.png "https://cellxgene.dev.single-cell.czi.technology/cell-guide/CL_0010008"
python image_crop.py ../content/cellguide/images/celltypelong.png 0 0 3200 1200 ../content/cellguide/images/descGPT.png
python image_crop.py ../content/cellguide/images/celltypelong.png 0 1200 2400 1200 ../content/cellguide/images/tree.png
python image_crop.py ../content/cellguide/images/celltypelong.png 0 2200 2400 800 ../content/cellguide/images/markergenes.png
python image_crop.py ../content/cellguide/images/celltypelong.png 0 3000 2400 1200 ../content/cellguide/images/references.png




####################################


#Obtain cropping coordinates for all rectangles in the image - experimental
#python element_rectangles.py ../content/dataportal/images/cxg_dp_collections_FullScreen.png ../content/dataportal/images/cxg_dp_collections_rectangles.txt
#python detect_sections.py ../content/dataportal/images/cxg_dp_collections_FullScreen.png ../content/dataportal/images/cxg_dp_collections_rectangles.txt


#Hosted explorer - spatial - full page
python screenshot_plus.py --width 3200 --height 1800 -o ../content/dataportal/images/cxg_dataportal_FullScreen.png "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/"


#Full length page - splash page example
python screenshotFull.py -o ~/Desktop/TestOutputFullLength.png "https://cellxgene.cziscience.com"

#HTML Elements
#python screenshot_html.py --display-tree "https://cellxgene.cziscience.com"

python screenshot_html.py "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/"

#Gene search HTML element test
python screenshot_element.py "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/" "/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div/input" --output ~/Desktop/TestOutputElement_genesearch.png
python screenshot_element.py "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/" -e "/html/body/div[1]/div/div[2]/" -o ~/Desktop/TestOutputElement_genesearch.png



python screenshot_element.py "https://cellxgene.cziscience.com/e/31b49393-4485-4998-9ef4-33e03c4c1789.cxg/" --list

python html_tree_with_metadata.py "https://cellxgene.cziscience.com"

# crop images

python image_crop.py ~/Desktop/TestOutputFull.png 100 100 200 300 ~/Desktop/TestOutputFullCrop.png


