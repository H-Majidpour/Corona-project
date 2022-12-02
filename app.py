from flask import Flask ,render_template
import Run_Spider
import Read_DB
import Draw_Plot


app = Flask(__name__, static_folder = "statics")


@app.route("/")
def crawl_info():

    # Step 1 : Runing Spider
    Run_Spider.run_spider()

    # Step 2 : Read Info
    info_dict = Read_DB.read_db()

    Coronavirus_Cases = info_dict.get("Coronavirus_Cases")
    Deaths = info_dict.get("Deaths")
    Recovered = info_dict.get("Recovered")
    Table_info = info_dict.get("Table_info")

    Country = Table_info[0]
    Total_Cases = Table_info[1]
    New_cases = Table_info[2]
    New_Deaths = Table_info[3]
    Total_Recovered = Table_info[4]
    New_Recovered = Table_info[5]
    Active_cases = Table_info[6]

    # Step 3 : Get Plot Image
    plot_src = Draw_Plot.get_plot(Country, Total_Cases)


    return render_template("index.html", Coronavirus_Cases = Coronavirus_Cases, Deaths = Deaths,
    Recovered = Recovered, Country = Country, Total_Cases = Total_Cases, New_cases = New_cases,
    New_Deaths = New_Deaths, Total_Recovered = Total_Recovered, New_Recovered = New_Recovered, 
    Active_cases = Active_cases, plot_src = plot_src)