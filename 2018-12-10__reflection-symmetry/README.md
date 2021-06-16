# Reflection Symmetry Detection in 2D Images

## Title

Reflection Symmetry Detection in Images: Applications to Computer
Vision and Visual Arts

## Abstract

Symmetry is a fundamental principle of visual perception to feel the
equally distributed weights within foreground objects inside an
image. It is used as a significant visual feature through various
computer vision applications (i.e. object detection and segmentation),
plus as an important composition measure in art domain (i.e. aesthetic
analysis). The development of symmetry detection has been improved
rapidly since last century. In this work, we mainly aims in detecting
reflection symmetry inside real-world images in a global scale. we
introduce several improvements to the reflection symmetry detection
pipeline. In particular, extraction and selection of the symmetrical
representation. First, we propose a novel approach that detects the
global salient edges inside an image using Log-Gabor filter banks,
then defines the symmetrical weights through textural and color around
these edges. This method wins a recent symmetry competition worldwide
in single and multiple cases. Second, we introduce a weighted kernel
density estimator to represent linear and directional symmetrical
candidates in a continuous way, then propose a joint Gaussian-vonMises
distance inside the mean-shift algorithm, to select the maxima peaks
defining well-defined candidate axes along side with their symmetrical
densities. Plus, we introduce a new challenging dataset of single
symmetry axes inside artistic photographs extracted from the
large-scale Aesthetic Visual Analysis (AVA) dataset. The proposed
contributions obtain superior results against state-of-art algorithms
among all public datasets, especially multiple cases in a global
scale. We conclude that the spatial and context information of each
candidate axis inside an image can be used as a local or global
symmetry measure for further image analysis and scene understanding
purposes.

## Bio

Mohamed Elawady (https://mawady.github.io) is a Computer Vision
Researcher at Qopius, Paris. He has studied in different European
universities: PhD in Computer Vision at Hubert Curien Laboratory, Lyon
University [France] (2014-2018). European Masters in Vision and
Robotics (VIBOT) with Erasmus Mundus Scholarship at Burgundy
University [France], Girona University [Spain] and Heriot-Watt
University [UK] (2012-2014). In addition, he is the winner of 2D
reflection symmetry competitions (among participants) in ICCV’17
Workshop: Detecting Symmetry in the Wild.

## Publications

Elawady, M., Ducottet, C., Alata, O., Barat, C., & Colantoni,
P. (2017). Wavelet-Based Reflection Symmetry Detection via Textural
and Color Histograms: Algorithm and Results. ICCV 2017 Workshop A
Challenge: Detecting Symmetry in the Wild.
http://openaccess.thecvf.com/content_ICCV_2017_workshops/papers/w24/Elawady_Wavelet-Based_Reflection_Symmetry_ICCV_2017_paper.pdf

Elawady, M., Alata, O., Ducottet, C., Barat, C., & Colantoni,
P. (2017). Multiple Reflection Symmetry Detection via
Linear-Directional Kernel Density Estimation. In International
Conference on Computer Analysis of Images and Patterns.
https://link.springer.com/chapter/10.1007/978-3-319-64689-3_28 -
https://hal-ujm.archives-ouvertes.fr/ujm-01637159/file/caip2017-multiple-reflection-final.pdf

Elawady, M., Barat, C., Ducottet, C., Colantoni, P. (2016). Global
Bilateral Symmetry Detection Using Multiscale Mirror Histograms. In
International Conference on Advanced Concepts for Intelligent Vision
Systems.
https://hal-ujm.archives-ouvertes.fr/ujm-01387193/file/paper107-cor.pdf
