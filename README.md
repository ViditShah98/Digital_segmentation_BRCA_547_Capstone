# Digital_segmentation_BRCA_547_Capstone

## Use Case
Automate the process by building a digital pipeline for multiple images to analyse like done for one test case.

Pipeline only for TILS so far. But how to separate different classes of immune cells i.e., macrophages and lymphocytes.

Following this we need to analyze percentage populations of immune cells close to tumor and far away from tumor boundaries.

Based on this, we need to reiterate if a supervised model is necessary or not.

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
