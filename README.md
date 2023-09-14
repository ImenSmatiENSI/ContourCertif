# ContourCertif
A NOVEL SYSTEM FOR DEEP CONTOUR CLASSIFIERS CERTIFICATION UNDER FILTERING ATTACKS

ContourCertif: a new system to certify deep contour classifiers against convolutional attacks. presented in [figure 1](lien_vers_l_image)
We use the abstract interpretation theory in order to formulate the Lower and Upper Bounds with abstract intervals to support other classes of advanced attacks including filtering.
For the abstract domain implementation, we use python. As abstract interpretation analyzer, we use DeepPoly solution that is maily based on [ERAN](https://github.com/eth-sri/eran) and [ELINA]([URL_du_lien](https://elina.ethz.ch/) libraries respectivelly coded in Python and C programming languages.

Various filters could be applied on a given contour. Among the well known filters, we cite the Gaussian kernels for instance see figure ![figure](lien_vers_l_image).

In order to study the efficiency of our algotrithme for abstract domains. we evaluate its robustness on different filter sizes. We present the robustness variation according to the kernel size in the caseof 100 contours from MPEG7 and MNIST datasets [2D-contours dataset](https://github.com/OueslatiRania/2D-contours-dataset).


