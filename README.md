# Digital_segmentation_BRCA_547_Capstone

## In order to use the code, you can create a virtual environment on a Windows system as follows: ##

Note: If you are using Unix or a conda environmnet, the steps might chnage accordingly.

**Step 1:** Clone the repository to your computer.

**Step 2:** Open the command prompt/shell and type `pip install virtualenv`

**Step 3:** In the command prompt/shell type `virtualenv environment_cluster`

**Step 4:** Create the virtual environment by typing `virtualenv environment_cluster`

**Step 5:** Activate the virtual environment by typing `.\environment_cluster\Scripts\activate`

**Step 6:** Enter the path to the repository on terminal `cd ./././Digital_segmentation_BRCA_547_Capstone`

**Step 7:** Install dependencies by typing `pip install -r requirements.txt`


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
