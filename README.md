# **Title: Topsis for MCMD Problems**



## **1. Methodology**

### *Step1*
* Normalization of the given decision table*
$$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

### *Step2*
* Weighted Normalized Decision Matrix- After normalizing we multiply the decision by there given weight corresponding to each column *
$$v_{ij} = w_j \times r_{ij}$$

### *Step3*
* Find the Ideal best and worst and then the Euclidean Distance from Ideal Best and Ideal Worst for each row*
$$S_i^+ = \sqrt{\sum (v_{ij} - V_j^+)^2}$$
$$S_i^- = \sqrt{\sum (v_{ij} - V_j^-)^2}$$

### *Step4*
*Find the performance value and rank them in descending order!*
$$P_i = \frac{S_i^-}{S_i^+ + S_i^-}$$


## **2. Description**
 ### **TOPSIS is a tool used to make smart decisions when there is no clear winner. Imagine you are buying a phone: one is cheap but has a bad camera, while another has a great camera but is too expensive. TOPSIS takes all these confusing trade-offs and uses math to rank the phones, finding the one that offers the best overall balance.**

 
## **3. Input / Output**
#### *Input*
<img width="453" height="237" alt="image" src="https://github.com/user-attachments/assets/391d8882-b3f4-441e-9f53-8810a0b7fc97" />

#### *Output*
<img width="536" height="200" alt="image" src="https://github.com/user-attachments/assets/de8fde99-adfd-4ac9-9c3f-cc28f0d20999" />


## **4. Local host link**
#### *Link:- http://127.0.0.1:5000*
<img width="566" height="330" alt="image" src="https://github.com/user-attachments/assets/2344e5f7-a346-4229-82a4-05f24a869bd5" />


## **5. Screenshot of the Interface**
<img width="511" height="587" alt="image" src="https://github.com/user-attachments/assets/c1f6ecc6-9628-460a-bbac-b543cbc20a59" />
