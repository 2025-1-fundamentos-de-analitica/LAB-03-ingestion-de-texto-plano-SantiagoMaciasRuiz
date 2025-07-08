import pandas as pd


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minúsculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """

    def clean_line(line):
        return " ".join(line.strip().split()).replace(".", "").strip()

    def process_header(header_line):
        headers = [h.strip() for h in header_line.split("  ") if h.strip()]
        headers[1] += " palabras clave"
        headers[2] += " palabras clave"
        return [header.lower().replace(" ", "_") for header in headers]

    def process_data_line(line, current_row):
        parts = [part.strip() for part in line.split("  ") if part.strip()]
        if parts[0].isdigit():
            if current_row:
                data.append(current_row.copy())
                current_row.clear()
            current_row.extend(
                [
                    int(parts[0]),
                    int(parts[1]),
                    float(parts[2].split()[0].replace(",", ".")),
                ]
            )
            percentage_index = line.find("%")
            current_row.append(clean_line(line[percentage_index + 1 :]))
        else:
            current_row[-1] += " " + clean_line(line)

    with open("files/input/clusters_report.txt") as file:
        lines = [line.strip() for line in file if "---" not in line and line.strip()]

    header = process_header(lines[0])

    data = []
    current_row = []
    for line in lines[2:]:
        process_data_line(line, current_row)

    if current_row:
        data.append(current_row)

    dataframe = pd.DataFrame(data, columns=header)
    return dataframe


pregunta_01()
