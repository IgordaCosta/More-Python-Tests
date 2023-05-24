import os
import csv

def get_import_statements(folder_path):
    import_statements = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                        if line.startswith('import') or line.startswith('from'):
                            import_statements.append(line)

    return import_statements

def save_import_statements_to_csv(import_statements, csv_file_path):
    with open(csv_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Import Statements'])
        for import_statement in import_statements:
            writer.writerow([import_statement])

def getAllPythonImportStatements(folder_path, csv_file_path):

    try:
        os.makedirs(folder_path)
    except:
        pass

    import_statements = get_import_statements(folder_path)
    import_statementsSet = set(import_statements)
    save_import_statements_to_csv(import_statementsSet, csv_file_path)


folder_path = r'C:\Users\Tigereye\Desktop\ImportPythonSaveLocations'
csv_file_path = folder_path + '\\outputLocaion\\output.csv'

getAllPythonImportStatements(folder_path, csv_file_path)
