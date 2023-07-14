# DIGHUM160: Digital Hermeneutics

![logo](img/backdrop-color.jpg)

[![DataHub](https://img.shields.io/badge/launch-datahub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Ftomvannuenen%2Fdighum160&urlpath=lab%2Ftree%2Fdighum160%2F) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the Jupyter Notebooks for DIGHUM160: Critical Digital Humanities, at the [UC Berkeley Digital Humanities Summer Minor](https://summerdigitalhumanities.berkeley.edu/).

## Course Summary
This course confronts hermeneutic philosophy with computational text analysis. Hermeneutics refers to a long-standing intellectual tradition in the humanities that focuses on the theory and methods of interpretation.

In the lectures and discussions, we will deal with leading hermeneutic philosophers focusing on issues such as dialogicality, perspective, reflexivity, and the scientific status of interpretation. These issues are relevant to the study of social media and discourse communities, and their particular interpretations of the world.

The other half of the course is project-based and involves research in Python to analyze a Reddit community of your choosing. You are not expected to have prior programming knowledge, and you are not graded on your coding skills. However, this course does make use of Jupyter Notebooks including Python code, so some exposure to Python will be highly beneficial.

## Installation Instructions

Before attending the workshop, you should install Python and Jupyter on your computer. If you need help, please make sure to come to the weekly seminar (see bCourses for more information).

Anaconda is software that allows you to run Python and Jupyter Notebooks on your computer. Installing Anaconda is the easiest way to make sure you have all the necessary software to run the materials for this workshop. Complete the following steps:

1. [Download and install Anaconda (Python 3.9 distribution)](https://www.anaconda.com/products/individual). Click "Download" and then click 64-bit "Graphical Installer" for your current operating system.

2. Download the materials in this repository:

* Click the green "Code" button in the top right of the repository information.
* Click "Download Zip".
* Extract/Unzip this file to a folder on your computer where you can easily access it (we recommend Desktop). If you need help on how to do this: [Mac](https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac) / [Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc).

3. You can install the package dependencies using the following terminal command (after navigating to the `DIGHUM160-main` folder):

```bash
pip install -r requirements.txt
 ```

## Run the code

Now that you have all the required software and materials, you need to run the code:

1. Open the Anaconda Navigator application. You should see the green snake logo appear on your screen. Note that this can take a few minutes to load up the first time.

2. Click the "Launch" button under "Jupyter Lab" and navigate through your file system to the `DIGHUM160` folder you downloaded above.

3. Navigate to the "Notebooks" folder, and to "Week1".

4. Open the `Preprocessing_Lesson.ipynb` file to begin.

5. Press Shift + Enter (or Ctrl + Enter) to run a cell.

## Is Python not working on your laptop?

If you do not have Anaconda installed and the materials loaded on your workshop by the time it starts, you can use the UC Berkeley DataHub to run the materials for these lessons. You can access the DataHub by clicking this button:

[![DataHub](https://img.shields.io/badge/launch-datahub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Ftomvannuenen%2Fdighum160&urlpath=lab%2Ftree%2Fdighum160%2F)

The DataHub downloads this repository, along with any necessary packages, and allows you to run the materials in a Jupyter notebook that is stored on UC Berkeley's servers. No installation is necessary from your end - you only need an internet browser and a CalNet ID to log in. By using the DataHub, you can save your work and come back to it at any time. When you want to return to your saved work, just go straight to [DataHub](https://datahub.berkeley.edu), sign in, and click on the `DIGHUM160` folder.

## Directories & Files

- **notebooks/**  Your Jupyter Notebooks, including accompanying video's on what is happening in them. You are expcted to swap out data with your own as soon as possible when using these.

- **data/**  The Data directory contains several example datasets we will work through.

- **img/**  Has the images used throughout this repository.

- **.gitignore**  A file for ignoring changes to this repository

- **README.md**  Contains the text on this page.

- **requirements.txt**  Python libraries needed to run this repo.

## DH Summer Minor

Learn more about the Berkeley Digital Humanities Summer Minor: https://summerdigitalhumanities.berkeley.edu/
