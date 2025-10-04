# CampusSwap

CampusSwap is a **full-stack marketplace platform** for college students to **buy, sell, and exchange items within same campus and between different campuses**. It provides a secure, user-friendly environment where students can list items for sale, browse listings, communicate with sellers, and complete transactions safely.

---

## **Features**

### **User**
- Register/login using **college email only** (`.edu` / `.ac`)  
- Browse, search, and purchase items  
- View personal **dashboard** with orders and listings  
- **Secure password** handling (hashed)  
- **Messaging** system for buyer-seller communication  

### **Seller**
- List items with **title, description, price, category, condition, purchase date, and image**  
- Manage and withdraw listings  

### **Admin**
- Approve or reject listings  
- Manage users and orders  

### **Frontend**
- Responsive UI with **Bootstrap 5**  
- Mobile-friendly design with grids and cards  

### **Backend**
- Django + PostgreSQL  
- RBAC (Role-Based Access Control)  
- Async **messaging microservice** using FastAPI  
- Decoupled architecture for scalability  

---
## Future Improvements 

-Image hosting on AWS S3

-Deployment on AWS / Render

-Advanced filters and search

-Notifications for orders and messages

------
## **Tech Stack**

-Backend: Django, PostgreSQL, FastAPI

-Frontend: HTML, CSS, Bootstrap 5, JavaScript

-Payment: Stripe / Razorpay sandbox

-Deployment: AWS free-tier / Render