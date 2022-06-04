[![Anaconda-Server Badge](https://anaconda.org/anaconda/anaconda/badges/platforms.svg)](https://anaconda.org/anaconda/anaconda)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Digital_segmentation_BRCA_547_Capstone

## Project Objective
The project is intended to segment Iymphocytes(T cells and B cells) and macrophages on the stained images. And we have already bulit an automaic 
pipeline that can extarct every patches from the Whole slide Image(WSI) of cancer tissue and using K-means clustering algorithm to get the 
overlayed immune cells.

## Use Cases
Generate clusters from an individual patch determine every component separately.</br>
Overlay a single, multiple or all clusters at once on a patch depending upon the analysis that clinician needs to perform.</br>
Automated process of an input WSI and multiple output overlayed patches.</br>
Automating components of analysis which are constant and enabling enough interventional capability for the user.</br>
Ability to classify different components within a particular subcluster of interest (if any exists)</br>

## Methodology
<img src=https://github.com/ViditShah98/Digital_segmentation_BRCA_547_Capstone/blob/main/Picture2.png />

## Installation
In order to use the code, you can create a virtual environment on a Windows system as follows:
Note: If you are using Unix or a conda environment, the steps might change accordingly.

**Step 1:** Clone the repository to your computer.

**Step 2:** Open the command prompt/shell and type `pip install virtualenv`

**Step 3:** In the command prompt/shell type `virtualenv environment_cluster`

**Step 4:** Create the virtual environment by typing `virtualenv environment_cluster`

**Step 5:** Activate the virtual environment by typing `.\environment_cluster\Scripts\activate`

**Step 6:** Enter the path to the repository on terminal `cd ./././Digital_segmentation_BRCA_547_Capstone`

**Step 7:** Install dependencies by typing `pip install -r requirements.txt`

## Example
<img src=https://github.com/ViditShah98/Digital_segmentation_BRCA_547_Capstone/blob/main/Picture1.png />

1. Extracted H&E-stained patch.

2. Digitally clustered patch.

3. Overlay of the digitally clustered patch.

4. Digital map of the segmented immune cells

5. Overlay of the segmented patch.

## Repo Structure
```
Digital_segmentation_BRCA_547_Capstone
-----
Digital_segmentation_BRCA_547_Capstone/
|-doc/
| |-example/paper/
| | |-_init_.py
| |-Use_cases_and_design_components.docx
|-tests/
| |-_init_.py  
|-cluster.py
|-requirements.txt
LICENSE
README.md
```
## Ongoing and Future Work

## Timeline
```mermaid
gantt
 title Timeline
 section To do
   Build a pipeline for multiple images processing (T-cells)     : 2022-04-23, 7d
   Build up several different pipelines for different immune cells    : 2022-04-30, 9d
   Create a UI containing all pipelines of different immune cells    : 2022-05-09, 7d
   Analyze percentage population of immune cells close and far away from tumor:    2022-05-16, 7d
   Add population analysis as a function in the UI:    2022-05-21, 7d
   Test UI and optimize process:    2022-05-27, 5d
   Prepare final presentation and finalize repository:    2022-05-31, 4d
 section Doing
   Buid a pipeline for one image processing (T-cells)    : 2022-04-14, 9d
 section Done
   Meet with sponsor    : 2022-04-01, 4d
   Buid use cases    : 2022-04-04, 5d
   Generate merged clusters and overlay images for the patches : 2022-04-08, 6d
   Make timeline and update repository : 2022-04-08, 6d
```
