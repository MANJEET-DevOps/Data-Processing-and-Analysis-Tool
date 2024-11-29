import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Global variable to hold the data
data = None

#---------------------------------------------- MAIN MENU---------------------------------------------------------------
def main():
    while True:
        print("*************************************************************************************************************")
        print("                                       DATA PROCESSING AND ANALYSIS TOOL             ")
        print("*************************************************************************************************************")
        print("\nMain Menu:")
        print("1. Read File")
        print("2. Manipulation")
        print("3. Analysis")
        print("4. Visualization")
        print("5. Exit")

        choice = input("Please enter your choice (1-5): ")

        if choice == '1':
            read_file()
        elif choice == '2':
            manipulation()
        elif choice == '3':
            analysis()
        elif choice == '4':
            visualization()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
# -------------------------------------------1. READ FILE--------------------------------------------------------------
def read_file():
    global data  # Use the global variable to store the data
    print("Reading file...")
    file_type = input("Which type of file do you want to read? (1 for Excel, 2 for CSV): ")

    if file_type == '1':
        file_path = input("Please enter the path to the Excel file: ").strip()  # remove leading and trailing whitespace characters
        try:
            data = pd.read_excel(file_path)
            print("Excel file read successfully!")
            print(data.head())  # Display the first few rows of the DataFrame
        except Exception as e:
            print(f"An error occurred while reading the Excel file: {e}")
    elif file_type == '2':
        file_path = input("Please enter the path to the CSV file: ").strip()  # sanitize input
        try:
            data = pd.read_csv(file_path)
            print("CSV file read successfully!")
            print(data.head())  # Display the first few rows of the DataFrame
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
    else:
        print("Invalid file type selected.")

#---------------------------------------2. DATA MANIPULATION------------------------------------------------------------
def manipulation():
    global data  # Access the global data variable
    if data is None:
        print("No data loaded. Please read a file first.")
        return

    while True:
        print("\nData Manipulation Options:")
        print("1. Display Data")
        print("2. Filter Data")
        print("3. Sort Data")
        print("4. Add a New Column")
        print("5. Delete a Row")
        print("6. Delete a Column")
        print("7. Delete Specific Data")
        print("8. Save Data")
        print("9. Exit Manipulation Menu")

        choice = input("Please enter your choice (1-9): ")

        if choice == '1':
            print(data.head())  # Display the first few rows of the DataFrame
        elif choice == '2':
            column_name = input("Enter the column name to filter by: ")
            filter_value = input("Enter the value to filter for: ")
            if column_name in data.columns:
                filtered_data = data[data[column_name] == filter_value]
                print(filtered_data)
            else:
                print("Column not found.")
        elif choice == '3':
            column_name = input("Enter the column name to sort by: ")
            if column_name in data.columns:
                sorted_data = data.sort_values(by=column_name)
                print(sorted_data)
            else:
                print("Column not found.")
        elif choice == '4':
            new_column_name = input("Enter the new column name: ")
            default_value = input("Enter the default value for the new column: ")
            data[new_column_name] = default_value
            print(f"New column '{new_column_name}' added with default value '{default_value}'.")
        elif choice == '5':
            row_index = int(input("Enter the index of the row to delete: "))
            if 0 <= row_index < len(data):
                data = data.drop(index=row_index)
                print(f"Row {row_index} deleted.")
            else:
                print("Invalid row index.")
        elif choice == '6':
            column_name = input("Enter the name of the column to delete: ")
            if column_name in data.columns:
                data = data.drop(columns=[column_name])
                print(f"Column '{column_name}' deleted.")
            else:
                print("Column not found.")
        elif choice == '7':
            column_name = input("Enter the column name to delete specific data from: ")
            if column_name in data.columns:
                value_to_delete = input("Enter the value to delete: ")
                data = data[data[column_name] != value_to_delete]
                print(f"Rows with value '{value_to_delete}' in column '{column_name}' deleted.")
            else:
                print("Column not found.")
        elif choice == '8':
            save_file()  # Call the save_file function
        elif choice == '9':
            print("Exiting Manipulation Menu.")
            break
        else:
            print("Invalid option. Please try again.")

def save_file():
    global data
    if data is None:
        print("No data to save. Please load or manipulate data first.")
        return

    file_type = input("Enter the file type to save (1 for Excel, 2 for CSV): ")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # Get the path to the Desktop
    file_name = input("Enter the name of the file (without extension): ")

    if file_type == '1':
        file_path = os.path.join(desktop_path, f"{file_name}.xlsx")
        try:
            data.to_excel(file_path, index=False)  # Save as Excel file
            print(f"Data saved successfully to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the Excel file: {e}")
    elif file_type == '2':
        file_path = os.path.join(desktop_path, f"{file_name}.csv")
        try:
            data.to_csv(file_path, index=False)  # Save as CSV file
            print(f"Data saved successfully to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the CSV file: {e}")
    else:
        print("Invalid file type selected.")

#--------------------------------------------3. DATA ANALYSIS-----------------------------------------------------------
def analysis():
    # Add your data analysis logic
        global data
        if data is None :
            print("No data loaded or DataFrame is empty. Please read a file first.")
            return

        while True:
            print("\nData Analysis Options:")
            print("1. Display Top Records")
            print("2. Display Bottom Records")
            print("3. Print Specific Column")
            print("4. Print Multiple Columns")
            print("5. Display Complete Statistics")
            print("6. Display DataFrame Information")
            print("7. Unique Values in a Column")
            print("8. Group By with Count")
            print("9. Group By with Multiple Functions")
            print("10. Aggregate Function")
            print("11. Pivoting")
            print("12. Exit Analysis Menu")

            choice = input("Please enter your choice (1-12): ")

            if choice == '1':
                n = int(input("Enter number of top records to display: "))
                print(data.head(n))
            elif choice == '2':
                n = int(input("Enter number of bottom records to display: "))
                print(data.tail(n))
            elif choice == '3':
                column_name = input("Enter the column name to print: ").strip()
                if column_name in data.columns:
                    print(data[column_name])
                else:
                    print(f"Column '{column_name}' does not exist.")
            elif choice == '4':
                columns = [col.strip() for col in input("Enter the column names separated by commas: ").split(',')]
                missing_columns = [col for col in columns if col not in data.columns]
                if missing_columns:
                    print(f"Columns not found: {', '.join(missing_columns)}")
                else:
                    print(data[columns])
            elif choice == '5':
                print("Complete Statistics:")
                print(data.describe(include='all'))
            elif choice == '6':
                print("DataFrame Information:")
                print(data.info())
            elif choice == '7':
                column_name = input("Enter the column to count unique values: ").strip()
                if column_name in data.columns:
                    print(data[column_name].nunique())
                else:
                    print(f"Column '{column_name}' does not exist.")
            elif choice == '8':
                group_column = input("Enter the column to group by: ").strip()
                if group_column in data.columns:
                    print(data.groupby(group_column).size())
                else:
                    print(f"Group column '{group_column}' does not exist.")
            elif choice == '9':
                group_column = input("Enter the column to group by: ").strip()
                if group_column in data.columns:
                    print(data.groupby(group_column).agg(['mean', 'sum', 'count']))
                else:
                    print(f"Group column '{group_column}' does not exist.")
            elif choice == '10':
                print("Aggregate Function Example:")
                print(data.agg(['mean', 'sum']))
            elif choice == '11':
                index_col = input("Enter the index column: ").strip()
                columns_col = input("Enter the columns to pivot: ").strip()
                values_col = input("Enter the values column: ").strip()
                if index_col in data.columns and columns_col in data.columns and values_col in data.columns:
                    try:
                        print(data.pivot(index=index_col, columns=columns_col, values=values_col))
                    except Exception as e:
                        print(f"Error during pivoting: {e}")
                else:
                    print(f"One or more columns for pivoting do not exist.")
            elif choice == '12':
                print("Exiting Analysis Menu.")
                break
            else:
                print("Invalid option. Please try again.")


#-------------------------------------------4. DATA VISUALIZATION-------------------------------------------------------
def visualization():
    print("Visualizing data...")
    # Add your data visualization logic here
    global data
    if data is None:
        print("No data loaded or DataFrame is empty. Please read a file first.")
        return
    while True:
        print("\nData Visualization Options:")
        print("1. Line Plot")
        print("2. Bar Chart")
        print("3. Histogram")
        print("4. Scatter Plot")
        print("5. Box Plot")
        print("6. Heatmap")
        print("7. Pie Chart")
        print("8. Pair Plot")
        print("9. Violin Plot")
        print("10. Count Plot")
        print("11. Facet Grid")
        print("12. Exit Visualization Menu")
        choice = input("Please enter your choice (1-12): ")

        if choice == '1':
            column_x = input("Enter the column name for the x-axis: ")
            column_y = input("Enter the column name for the y-axis: ")
            if column_x in data.columns and column_y in data.columns:
                plt.figure(figsize=(10, 6))
                plt.plot(data[column_x], data[column_y])
                plt.title(f'Line Plot of {column_y} vs {column_x}')
                plt.xlabel(column_x)
                plt.ylabel(column_y)
                plt.show()
            else:
                print("One or both columns do not exist.")
        elif choice == '2':
            column_x = input("Enter the column name for the x-axis: ")
            column_y = input("Enter the column name for the y-axis (or leave blank for counts): ")
            plt.figure(figsize=(10, 6))
            if column_y:
                sns.barplot(x=column_x, y=column_y, data=data)
            else:
                sns.countplot(x=column_x, data=data)
            plt.title(f'Bar Chart of {column_x}')
            plt.show()
        elif choice == '3':
            column_name = input("Enter the column name for the histogram: ")
            if column_name in data.columns:
                plt.figure(figsize=(10, 6))
                plt.hist(data[column_name], bins=30, edgecolor='black')
                plt.title(f'Histogram of {column_name}')
                plt.xlabel(column_name)
                plt.ylabel('Frequency')
                plt.show()
            else:
                print("Column does not exist.")
        elif choice == '4':
            column_x = input("Enter the column name for the x-axis: ")
            column_y = input("Enter the column name for the y-axis: ")
            if column_x in data.columns and column_y in data.columns:
                plt.figure(figsize=(10, 6))
                plt.scatter(data[column_x], data[column_y])
                plt.title(f'Scatter Plot of {column_y} vs {column_x}')
                plt.xlabel(column_x)
                plt.ylabel(column_y)
                plt.show()
            else:
                print("One or both columns do not exist.")
        elif choice == '5':
            column_name = input("Enter the column name for the box plot: ")
            if column_name in data.columns:
                plt.figure(figsize=(10, 6))
                sns.boxplot(y=data[column_name])
                plt.title(f'Box Plot of {column_name}')
                plt.show()
            else:
                print("Column does not exist.")
        elif choice == '6':
            plt.figure(figsize=(10, 6))
            sns.heatmap(data.corr(), annot=True, cmap='cool warm', fmt='.2f')
            plt.title('Heatmap of Correlation Matrix')
            plt.show()

        elif choice == '7':
            column_name = input("Enter the column name for the pie chart: ")
            if column_name in data.columns:
                plt.figure(figsize=(8, 8))
                data[column_name].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                plt.title(f'Pie Chart of {column_name}')
                plt.ylabel('')  # Hide the y-label
                plt.show()
            else:
                print("Column does not exist.")

        elif choice == '8':
            sns.pairplot(data)
            plt.title('Pair Plot of DataFrame')
            plt.show()

        elif choice == '9':
            column_name = input("Enter the column name for the violin plot: ")
            if column_name in data.columns:
                plt.figure(figsize=(10, 6))
                sns.violinplot(y=data[column_name])
                plt.title(f'Violin Plot of {column_name}')
                plt.show()
            else:
               print("Column does not exist.")

        elif choice == '10':
            column_x = input("Enter the column name for the x-axis (categorical): ")
            column_y = input("Enter the column name for the y-axis (numerical): ")
            if column_x in data.columns and column_y in data.columns:
                plt.figure(figsize=(10, 6))
                sns.countplot(x=column_x, data=data)
                plt.title(f'Count Plot of {column_x}')
                plt.show()
            else:
               print("One or both columns do not exist.")

        elif choice == '11':
            column_x = input("Enter the column name for the rows (categorical): ")
            column_y = input("Enter the column name for the columns (categorical): ")
            if column_x in data.columns and column_y in data.columns:
                 g = sns.FacetGrid(data, row=column_x, col=column_y, margin_titles=True)
                 g.map(sns.histplot, 'value')  # Replace 'value' with the appropriate numerical column
                 g.set_titles(col_template="{col_name}", row_template="{row_name}")
                 plt.show()
            else:
               print("One or both columns do not exist.")

        elif choice == '12':
            print("Exiting Visualization Menu.")
            break

        else:
          print('Invalid option. Please try again.')


if __name__ == "__main__":
    main()