library(shiny)
library(ggplot2)
#Import datas from lille
data=read.csv("https://opendata.lillemetropole.fr/explore/dataset/indice-qualite-de-lair/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true", head=TRUE, sep=";")
keeps = c("date_ech", "valeur")
data = data[keeps]
data$date_ech <- as.Date(data$date_ech, "%Y-%m-%d")
#Import datas from our CSv with the censors on the roof
data2=read.csv("RecuperationDonnees.csv", head=TRUE, sep=";")
keeps2 = c("TempExt", "HygroExt", "TempExt","PanneauS","Batterie","time")
data2 = data2[keeps2]
data2$time <- as.POSIXct(data2$time)

ui <- navbarPage("AirIQ - First visualization of the datas",
    #First page
    tabPanel("Air index histogram",
        sidebarLayout(
            sidebarPanel(
                sliderInput("bins",
                            "Number of bins:",
                            min = 1,
                            max = 10,
                            value = c(0,10))
                ),
            
            mainPanel(
                plotOutput("histoPlot")
            )
        )
    ),
    # Second page
    tabPanel("Air index quality",
        sidebarLayout(
            sidebarPanel(
                    dateRangeInput('dateRangeIQ',
                        label = 'Date range input: yyyy-mm-dd',
                        start = as.Date("2018-01-01"), end = Sys.Date())
                    ),
            # Show
            mainPanel(
                plotOutput("dateRangeIQ")
            )
        )
    ),
    # Third page
    tabPanel("Temperature",
             sidebarLayout(
                 sidebarPanel(
                     dateRangeInput('dateRangeTemp',
                                    label = 'Date range input: yyyy-mm-dd',
                                    start = as.Date("2019-05-22"), end = Sys.Date()+1)
                 ),
                 # Show
                 mainPanel(
                     plotOutput("dateRangeTemp")
                 )
             )
    ),
    # Fourth page
    tabPanel("Humidity",
             sidebarLayout(
                 sidebarPanel(
                     dateRangeInput('dateRangeHum',
                                    label = 'Date range input: yyyy-mm-dd',
                                    start = as.Date("2019-05-22"), end = Sys.Date()+1)
                 ),
                 # Show
                 mainPanel(
                     plotOutput("dateRangeHum")
                 )
             )
    ),
    # Fifth page
    tabPanel("Sun exposure",
             sidebarLayout(
                 sidebarPanel(
                     dateRangeInput('dateRangeSun',
                                    label = 'Date range input: yyyy-mm-dd',
                                    start = as.Date("2019-05-22"), end = Sys.Date()+1)
                 ),
                 # Show
                 mainPanel(
                     plotOutput("dateRangeSun")
                 )
             )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    output$histoPlot <- renderPlot({
        qplot(data$valeur,
              geom="histogram",
              breaks=seq(input$bins[1], input$bins[2], by = 1),
              binwidth = 1,
              fill=I("orange"), 
              col=I("red"),
              main = "Histogram of IQ values", 
              xlab = "Index",
              xlim=c(1,10))
    })
    
    output$dateRangeIQ <- renderPlot({
        ggplot(data = data, aes(x = date_ech, y = valeur))+
            geom_line(color = "orange", size = 0.5)+ xlim(input$dateRangeIQ)
    })
    
    output$dateRangeTemp <- renderPlot({
        ggplot(data = data2, aes(x = time, y = TempExt))+
            geom_line(color = "blue", size = 0.5)+ ggtitle("Temperature (degree celsius)")+ 
            xlim(as.POSIXct(input$dateRangeTemp))
    })
    
    output$dateRangeHum <- renderPlot({
        ggplot(data = data2, aes(x = time, y = HygroExt))+
            geom_line(color = "chartreuse3", size = 0.5)+ ggtitle("Humidity (%)")+ 
            xlim(as.POSIXct(input$dateRangeHum))
    })
    output$dateRangeSun <- renderPlot({
        ggplot(data = data2, aes(x = time, y = PanneauS))+
            geom_line(color = "deeppink", size = 0.5)+ ggtitle("Sun exposure of the solar pannels (in Volts)")+ 
            xlim(as.POSIXct(input$dateRangeSun))
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
