import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

file = 'C:/Users/jdebn/OneDrive/Desktop/PYTHON/flipkart_laptops_under_80k.csv'
df = pd.read_csv(file)


root = tk.Tk()
root.title("Laptop Data Visualization")


def display_histogram():
    
    page_window = tk.Toplevel(root)
    page_window.title("Enter Page Number")
    
  
    page_label = tk.Label(page_window, text="Enter the page number(1-10) of the laptop listings you want to view (24 laptops per page):")
    page_label.grid(row=0, column=0, padx=100, pady=10)

    page_entry = tk.Entry(page_window)
    page_entry.grid(row=1, column=0, padx=100, pady=10)

    
    def show_histogram():
        nonlocal page_window 
        page_num = int(page_entry.get())
        if page_num > 0 and page_num < 11:
            n = (page_num * 24) - 1
            m = (page_num - 1) * 24
            plt.figure(figsize=(10, 6))
            sns.histplot(df.loc[m:n, 'Prices'], bins=50)
            plt.show()
            page_window.destroy()  
        else:
            print('Wrong input')
            
    
    button = tk.Button(page_window, text="Show Histogram", command=show_histogram,fg='black',bg='light steel blue')
    button.grid(row=2, column=1, padx=10, pady=10)

        

def display_top_rated():
    review_counts = df.groupby("Product_name")["Ratings"].sum().reset_index()
    review_counts = review_counts.sort_values(by=["Ratings"], ascending=False)
    sns.barplot(x="Ratings", y="Product_name", data=review_counts[:10],palette="Blues_d")
    plt.title("Top 10 Rated Laptops")
    plt.xlabel("Total Ratings")
    plt.ylabel("Product Name")
    plt.show()


def display_rating_vs_processor():
    cols = ['Processor', 'Ratings']
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=cols[0], y=cols[1], data=df)
    plt.title('Rating vs Processor')
    plt.xlabel('Processor')
    plt.ylabel('Rating')
    plt.show()


label = tk.Label(root, text="Choose what you want to see :)")
label.grid(row=0, column=1, padx=10, pady=10)

button1 = tk.Button(root, text="Histogram of laptop prices", command=display_histogram,width=100,fg='black',bg='light steel blue')
button1.grid(row=1, column=1, padx=100, pady=10)


button2 = tk.Button(root, text="Top 10 rated laptops", command=display_top_rated,width=100,fg='black',bg='light steel blue')
button2.grid(row=2, column=1,padx=100, pady=10)

button3 = tk.Button(root, text="Rating vs processor", command=display_rating_vs_processor,width=100,fg='black',bg='light steel blue')
button3.grid(row=3, column=1,padx=100, pady=10)

button4 = tk.Button(root, text="Exit", command=root.destroy,width=100,fg='black',bg='light steel blue')
button4.grid(row=4, column=1, padx=100, pady=10)




root.mainloop()
