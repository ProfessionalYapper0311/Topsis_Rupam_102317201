# **Title: Topsis for MCMD Problems**


## **1. Methodology**

###*Step1*
* Normalization of the given decision table*
$$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

###*Step2*
* Weighted Normalized Decision Matrix- After normalizing we multiply the decision by there given weight corresponding to each column *
$$v_{ij} = w_j \times r_{ij}$$

###*Step3*
* Find the Ideal best and worst and then the Euclidean Distance from Ideal Best and Ideal Worst for each row*
$$S_i^+ = \sqrt{\sum (v_{ij} - V_j^+)^2}$$
$$S_i^- = \sqrt{\sum (v_{ij} - V_j^-)^2}$$

###*Step4*
*Find the performance value and rank them in descending order!*
$$P_i = \frac{S_i^-}{S_i^+ + S_i^-}$$


## **2. Description**
 ### **TOPSIS is a tool used to make smart decisions when there is no clear winner. Imagine you are buying a phone: one is cheap but has a bad camera, while another has a great camera but is too expensive. TOPSIS takes all these confusing trade-offs and uses math to rank the phones, finding the one that offers the best overall balance.**
## **3. Input / Output**

## **4. Local host link**

## **5. Screenshot of the Interface**
