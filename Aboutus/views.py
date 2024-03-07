from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import AboutUs
#from django.http import HttpResponse



# def Aboutus(request):
#     return HttpResponse("Aboutus")


# def Aboutus(request):
#     return render(request, "Aboutus/aboutus.html")

def Aboutus(request):
 

    template = "Aboutus/aboutus.html"
    context = {
               
       'title': "We Implement Geospatial Solutions for Sustainable Development",
       'description' : "The Centre for Remote Sensing and Geographic Information Services (CERSGIS) was established in 1999 by the University of Ghana and the Environmental Protection Agency of Ghana (EPA). As a self-supporting organization, CERSGIS was mandated to provide GIS and Remote Sensing services using Geospatial technologies to provide decision support and planning tools for sustainable social and economic development to Government, NGOs, Research Institutions and the Private Sector. The Centre is located at the Department of Geography and Resource Development, University of Ghana, Legon In addition, the Centre provides inter alia, services in the development of Spatial Data Infrastructure Satellite Image processing, Spatial Database development and Web-based applications for spatial land use/land cover mapping and planning, desertification, flood hazard mapping, spatial modeling, vulnerability assessment and capacity enhancement programs in Geographic Information System development.Over the pasdt decade, CERSGIS has expanded its capacity by the succesful execution of Geographic Information Systems (GIS) and Remote Sensing related projects for the Ghana Government - Ministries, Departments and Agencies, the UN Agencies and Development Partners such as AfDB, European Union (EU), World Bank, GIZ, JICA, DFID and the Ghana Armed Forces (GAF), African Union (AU) and the United States Agency for International Development (USAID).CERSGIS is a partner currently involved in the implementation of the sub-regional program, SERVIR West Africa, that promotes the use of Remote Sensing technology to help stakeholders and decision makers address pertinent issues on agriculture and food insecurity, land cover/land use and ecosystems, weather and climate,water resources and",
       'our_mission': "Our mission is to support development planning with geo-information technologies, generate geo-information products for decision making, build capacity, and making spatial data widely available",
       'our_vision': "Our vision is to provide geospatial solutions for sustainable development",
       'why_us': "We are here to offer GIS and Remote Sensing services to provide decision support and planning tools for sustainable social and economic development to Governments, NGOs, Research Institutions and the Private sectors",
       'meet_our_team': "Surf throught the collective CERSGIS team and the various assigned portfolios"
     
    }
    return render(request, template ,context)
    
   