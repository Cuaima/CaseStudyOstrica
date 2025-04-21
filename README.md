# **Sales Analytics Dashboard**

A Streamlit-based interactive dashboard for analyzing sales trends, newsletter opt-in rates, and revenue performance at **DataVisuals Inc.**

---

## 🔧 **1. Installation & Setup**

### **1.1 Prerequisites**

Make sure you have **Python 3.8+** installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).

### **1.2 Unzip the Project Files**
If you have received the project in a zipped file, unzip it using one of the following methods:
- **Windows:** Right-click the `.zip` file and select **Extract All.**
- **macOS:** Double-click the `.zip` to extract it.
- **Linux:** Use the terminal command:
```bash
unzip CaseStudyOstrica.zip
```
Then, navigate into the project folder in your terminal:
This step is different depending on your operating system (OS).
Here are some tips for each OS:

#### On Windows:
1. Press **Win + R** on your keyboard to open the **Run** dialog.
2. Type `cmd` for Command Prompt or `powershell` for PowerShell and press **Enter.**

#### On macOS:
1. Open **Finder.**
2. Go to the **Applications** folder -> Utilities -> Terminal.

#### On Linux:
1. Press **Ctr + Alt + T**.

```bash
cd CaseStudyOstrica
```
Note that the project might be located in a different folder, depending on where it is saved.

### **1.3 Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **1.4 Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **2. How to Run the Project**

### **2.1 Run the Streamlit Dashboard**

```bash
python3 main.py
```

This will open a browser window displaying the **interactive sales dashboard**.

### **2.2 Expected Output**

The dashboard includes:  
- Monthly & Quarterly Sales Trends.
- Newsletter Opt-in Comparison (vs. 65% Target).
- Revenue Comparison by Sales Manager.
- Filters to Explore Data (Date, Sales Manager, City).

---

## **3. Implemented Features**

### **Data Processing (data_processing.py)**

- Loads **Salesdata_case.xlsx** & **Customerdata_case.xlsx.**
- Transforms the files into **Sales.csv** & **Customer.csv.**
- Cleans & merges datasets.
- Converts **dates** to datetime format.
- Adds **Sales Manager** classification (Emma vs. Max).
- Adds **Quarterly** and **Monthly** data.

### **Visualizations (visualizations.py)**

- **Sales Trends** → Monthly/Quarterly bar & line charts.
- **Newsletter Opt-in Bar & Pie Chart** → Compares opt-in rate to **65% target**
- **Revenue Bar Chart** → Grouped bars for **Emma vs. Max**

### **Interactive Dashboard (interactive_dashboard.py)**

- **Filters** → Dropdowns & sliders for **date, city, sales manager.**
- **Interactive Elements** → Users can explore sales metrics dynamically.
- **KPIs Displayed** → Total Sales, Avg Order Value, Top-Selling Cities.

---

## **4. Assumptions & Challenges**

### **4.1 Assumptions**

- **Sales & Customer data is in xlsx format** and contains clean numeric values with specific names.
- **Customers file has unique Customer_IDs** and correctly maps to sales.
- **Amsterdam, ‘s-Gravenhage, ‘s-Hertogenbosch & Delft** belong to Emma; all others belong to Max.

### **4.2 Challenges Faced**

- **Merging Data:** Sales & Customers had different column names for Customer IDs. **Solution:** Renamed columns before merging.
- **Limited Knowledge of the Libraries:** As a first-year student, in my first trimester of my career, this was my first time using most of the libraries used in this project.
- **Organization:** It was difficult to keep the code modular and DRY.
- **Choosing technologies:** When assigning sales managers, numpy would have been more efficient for a large data set; however, pandas would be better for more complex logic. In this instance, I chose to use Pandas because it would give flexibility to more complex logic in the future, and also because the data was (at this time) not very large. However, should the dataset be updated and grow, this design feature should be reconsidered.

---

## **5. Future Improvements**

- The missing data is deleted in this implementation, which is not the best solution when dealing with missing data in general. I did not spend enough time with the data to know what (or if) there was a pattern to missing data. A possible solution would have been data imputation (ideally using neural networks). 
- Improve the **design** of the graphs to look better and be better at explaining the data. For the data created with Matplotlib:
    - The revenue per manager sales there are euros combined with percentages on the label of the graph, which is confusing, and the Y axis says euros, but it only goes up to 1.2, and it's not clear if that is in millions or thousands.
    - The target Opt-in graph could be shown better using a dotted line on the Y axis at the 65% mark.
    - The charts and plots are not visually appealing.
- Write more Pythonic code and follow the PEP guidelines.
- Regarding **missing values** and **anonymization**: I was not sure if removing the missing value rows was the best practice I could have used. Same with the customer's personal data anonymization. I considered using Faker to simulate names and postal codes, but I was not sure if this is the industry standard. 
- Make the files more modular, and make more functions out of the interactive dashboard. Perhaps making a class for some of the data objects (sales, customer, merged data), to make the code more comprehensive.
- Add **tests** for both the code and the pipeline. And refactor the `try` and `except` code into something more Pythonic.
- Add **geographic heatmap** for revenue distribution.
- Improve **date filtering** for better performance.
- Enable **user-uploaded datasets** for real-time analysis. This means that the files to be loaded would need to be curated, but it would enhance the flexibility of the application.

---

This **README.md** covers everything needed to install, run, and understand the project! 

Would you like me to adjust anything based on your specific implementation? 
