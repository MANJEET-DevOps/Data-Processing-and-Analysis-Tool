import pandas as pd
import os.path
import matplotlib.pyplot as plt
import seaborn as sns

print("WELCOMED TO DATA ANALYSIS TOOL")
print("THERE ARE FEW STEPS THAT YOU NEED TO FOLLOW TO PERFORM VARIOUS OPERATIONS ON DATA")
your_file = input("Enter the path to your data here:")
if not os.path.exists(your_file):  # to check the file existence
    print("SORRY NO SUCH FILE EXISTS CHECK THE FILE PATH AND TRY AGAIN:")
else:
    if your_file.endswith(".csv"):  # to check the type of file
        df = pd.read_csv(your_file)
        print(df)
    elif your_file.endswith((".xlsx")):
        df = pd.read_excel(your_file)
        print(df)
    else:
        print("Error: Unsupported file format. Please provide a CSV or Excel file.")

print("YOUR FILE IS SUCCESSFULLY IMPORTED :")
################################################### OPERATIONS TO BE CHOOSED #################################################

while True:
    print("\nPlease choose an operation:")
    print("1. Data Manipulation")
    print("2. Data Analysis")
    print("3. Data Visualization")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")
    if choice == "1":

        # 1- DATA MANIPULATION-----------------------------------------------------------------------------------------------------

        print("data manipulation is selected:")
        print("\n Please select the operation for data manipulation")
        print("1. REMOVE EMPTY CELLS")
        print("2. REMOVE DUPLICATES")
        print("3. FILL EMPTY CELLS")
        print("4. Exit")

        Choose_method = input("Enter the number of your choice: ")
        if Choose_method == "1":
            df = df.dropna()
            print(df)
        elif Choose_method == "2":
            df = df.drop_duplicates()
            print(df)
        elif Choose_method == "3":
            n = int(input("enter number of top record to display:"))
            df = df.fillna(n)
            print(df)
        elif Choose_method == "4":
            break
        else:
            print("invalid option try again")
    elif choice == "2":

        # 2- DATA ANALYSIS--------------------------------------------------------------------------------------------------

        print("data analysis is selected")
        print("\n Please select the operation for data analysis")
        print("1. DISPLAY TOP RECORDS")
        print("2. DISPLAY BOTTOM RECORDS")
        print("3. PRINT SPECIFIC COLUMN ")
        print("4. PRINT MULTIPLE COLUMN ")
        print("5. DISPLAY COMPLETE STATISTICS")
        print("6. DISPLAY DATAFRAME INFORMATION ")
        print("7. UNIQUE VALUES IN A COLUMN")
        print("8. GROUP BY WITH MULTIPLE FUNCTIONS ")
        print("9. AGGREGATE FUNCTIONS ")
        print("10.PIVOTING")
        print("11.EXIT ANALYSIS MENU")

        Choose_analysis = input("Enter the number of your choice: ")
        if Choose_analysis == "1":
            n = int(input("enter number of top record to display:"))
            df = df.head(n)
            print(df)
        elif Choose_analysis == "2":
            n = int(input("enter number of top record to display:"))
            df = df.tail(n)
            print(df)
        elif Choose_analysis == "3":
            column_name = input("enter your column name").strip()
            if column_name in df.columns:
                print(df[column_name])
            else:
                print(f"column'{column_name}'does not exist:")
        elif Choose_analysis == "4":
            columns = [col.strip() for col in input("Enter the column names separated by commas: ").split(',')]
            missing_columns = [col for col in columns if col not in df.columns]
            if missing_columns:
                print(f"Columns not found: {', '.join(missing_columns)}")
            else:
                print(df[columns])
        elif Choose_analysis == '5':
            print("Complete Statistics:")
            print(df.describe(include='all'))
        elif Choose_analysis == '6':
            print("DataFrame Information:")
            print(df.info())
        elif Choose_analysis == '7':
            column_name = input("Enter the column to count unique values: ").strip()
            if column_name in df.columns:
                print(df[column_name].nunique())
            else:
                print(f"Column '{column_name}' does not exist.")
        elif Choose_analysis == "8":
            group_column = input("Enter the column to group by: ").strip()
            if group_column in df.columns:
                agg_column = input("Enter the column to aggregate: ").strip()
                if agg_column in df.columns:
                    print(df.groupby(group_column).agg({agg_column: ['mean', 'sum']}))
                else:
                    print(f"Column '{agg_column}' not found.")
            else:
                print(f"Column '{group_column}' does not exist.")
        elif Choose_analysis == "9":
            group_column = input("Enter column to group by: ").strip()
            agg_column = input("Enter column to aggregate: ").strip()
            if group_column in df.columns and agg_column in df.columns:
                print(df.groupby(group_column).agg({agg_column: 'mean'}))
            else:
                print(f"Columns '{group_column}' or '{agg_column}' not found.")
        elif Choose_analysis == "10":
            index_column = input("Enter the index column: ").strip()
            columns = input("Enter the columns to pivot: ").strip()
            values = input("Enter the values to aggregate: ").strip()

            if index_column in df.columns and columns in df.columns and values in df.columns:
                print(df.pivot_table(index=index_column, columns=columns, values=values, aggfunc='mean'))
            else:
                print(f"One of the columns '{index_column}', '{columns}', or '{values}' not found.")

        elif Choose_analysis == "11":
            print("Exit")
            break
        else:
            print("invalid option try again later:")

    # 3- DATA VISUALIZATION----------------------------------------------------------------------------------------------------

    elif choice == "3":

        print("data visualization is selected")
        print("\n Please select the operation for data visualization")
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

        if choice == '1':
            column_x = input("Enter the column name for the x-axis: ")
            column_y = input("Enter the column name for the y-axis: ")

            if column_x in df.columns and column_y in df.columns:
                plt.figure(figsize=(10, 6))
                plt.plot(df[column_x], df[column_y])
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
                sns.barplot(x=column_x, y=column_y, data=df)
            else:
                sns.countplot(x=column_x, data=df)
            plt.title(f'Bar Chart of {column_x}')
            plt.show()

        elif choice == '3':
            column_name = input("Enter the column name for the histogram: ")
            if column_name in df.columns:
                plt.figure(figsize=(10, 6))
                plt.hist(df[column_name], bins=30, edgecolor='black')
                plt.title(f'Histogram of {column_name}')
                plt.xlabel(column_name)
                plt.ylabel('Frequency')
                plt.show()
            else:
                print("Column does not exist.")

        elif choice == "4":
            column_x = input("Enter the column name for the x-axis: ")
            column_y = input("Enter the column name for the y-axis: ")
            if column_x in df.columns and column_y in df.columns:
                plt.figure(figsize=(10, 6))
                plt.scatter(df[column_x], df[column_y])
                plt.title(f'Scatter Plot of {column_y} vs {column_x}')
                plt.xlabel(column_x)
                plt.ylabel(column_y)
                plt.show()
            else:
                print("One or both columns do not exist.")

        elif choice == '5':
            column_name = input("Enter the column name for the box plot: ")
            if column_name in df.columns:
                plt.figure(figsize=(10, 6))
                sns.boxplot(y=df[column_name])
                plt.title(f'Box Plot of {column_name}')
                plt.show()
            else:
                print("Column does not exist.")

        elif choice == '6':
            plt.figure(figsize=(10, 6))
            sns.heatmap(df.corr(), annot=True, cmap='cool warm', fmt='.2f')
            plt.title('Heatmap of Correlation Matrix')
            plt.show()

        elif choice == '7':
            column_name = input("Enter the column name for the pie chart: ")
            if column_name in df.columns:
                plt.figure(figsize=(8, 8))
                df[column_name].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                plt.title(f'Pie Chart of {column_name}')
                plt.ylabel('')  # Hide the y-label
                plt.show()
            else:
                print("Column does not exist.")

        elif choice == '8':
            sns.pairplot(df)
            plt.title('Pair Plot of DataFrame')
            plt.show()

        elif choice == '9':
            column_name = input("Enter the column name for the violin plot: ")
            if column_name in df.columns:
                plt.figure(figsize=(10, 6))
                sns.violinplot(y=df[column_name])
                plt.title(f'Violin Plot of {column_name}')
                plt.show()
            else:
                print("Column does not exist.")

        elif choice == '10':
            column_x = input("Enter the column name for the x-axis (categorical): ")
            column_y = input("Enter the column name for the y-axis (numerical): ")
            if column_x in df.columns and column_y in df.columns:
                plt.figure(figsize=(10, 6))
                sns.countplot(x=column_x, data=df)
                plt.title(f'Count Plot of {column_x}')
                plt.show()
            else:
                print("One or both columns do not exist.")

        elif choice == '11':
            column_x = input("Enter the column name for the rows (categorical): ")
            column_y = input("Enter the column name for the columns (categorical): ")
            if column_x in df.columns and column_y in df.columns:
                g = sns.FacetGrid(df, row=column_x, col=column_y, margin_titles=True)
                g.map(sns.histplot, 'value')  # Replace 'value' with the appropriate numerical column
                g.set_titles(col_template="{col_name}", row_template="{row_name}")
                plt.show()
            else:
                print("One or both columns do not exist.")

        elif choice == '12':
            print("Exit.")
            break

        else:
            print("Invalid option. Please try again.")