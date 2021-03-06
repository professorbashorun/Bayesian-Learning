"""horseid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from api import views







urlpatterns = [


	#API URLs 													REPONSE FUNCTIONS
    url(r'^admin/', 											admin.site.urls),
    url(r'^variables/', 										views.VariablesList.as_view()),
    url(r'^is_started/', 										views.IsStarted.as_view()),
    url(r'^network_data/', 										views.NetworkData.as_view()),
    url(r'^view_network/', 										views.ViewNetwork.as_view(), name="view_network"),
    url(r'^update/', 							     			views.UpdateAndQuery.as_view()),
    url(r'^model/start/',                                       views.HorseIDBayesianNetworkAPI.start.as_view()),
    url(r'^model/build/',										views.HorseIDBayesianNetworkAPI.build.as_view()),
    url(r'^model/run/',											views.HorseIDBayesianNetworkAPI.run.as_view()),
    url(r'^model/update/',										views.HorseIDBayesianNetworkAPI.update.as_view()),
    url(r'^model/initialise_space/',							views.HorseIDBayesianNetworkAPI.initialise_space.as_view()),
    url(r'^model/set_universe/',								views.HorseIDBayesianNetworkAPI.set_universe.as_view()),
    url(r'^model/clear_values/',								views.HorseIDBayesianNetworkAPI.clear_values.as_view()),
    url(r'^model/use_default_values/',							views.HorseIDBayesianNetworkAPI.use_default_values.as_view()),
    url(r'^model/declare_variables/',							views.HorseIDBayesianNetworkAPI.declare_variables.as_view()),
    url(r'^model/update_values/',								views.HorseIDBayesianNetworkAPI.update_values.as_view()),
    url(r'^model/load_sizes/',									views.HorseIDBayesianNetworkAPI.load_sizes.as_view()),
    url(r'^model/set_evidences/',							    views.HorseIDBayesianNetworkAPI.set_evidences.as_view()),
    url(r'^model/load_evidences/',                              views.HorseIDBayesianNetworkAPI.load_evidences.as_view()),
    url(r'^model/set_cpds/',									views.HorseIDBayesianNetworkAPI.set_cpds.as_view()),#stop here
    url(r'^model/load_cpds/',									views.HorseIDBayesianNetworkAPI.load_cpds.as_view()),
    url(r'^model/load_default_graph/',							views.HorseIDBayesianNetworkAPI.load_default_graph.as_view()),
    url(r'^model/draw_default_graph/',                          views.HorseIDBayesianNetworkAPI.draw_default_graph.as_view()),
    url(r'^model/load_graph/',                                  views.HorseIDBayesianNetworkAPI.load_graph.as_view()),
    url(r'^model/draw_graph/',									views.HorseIDBayesianNetworkAPI.draw_graph.as_view()),
    url(r'^model/build_model/',									views.HorseIDBayesianNetworkAPI.build_model.as_view()),
    url(r'^model/load_cpds_to_model/',							views.HorseIDBayesianNetworkAPI.load_cpds_to_model.as_view()),
    url(r'^model/load_model/',									views.HorseIDBayesianNetworkAPI.load_model.as_view()),
    url(r'^model/train_model/',									views.HorseIDBayesianNetworkAPI.train_model.as_view()),
    url(r'^model/update_model/',								views.HorseIDBayesianNetworkAPI.update_model.as_view()),
    url(r'^model/test_model/',									views.HorseIDBayesianNetworkAPI.test_model.as_view()),
    url(r'^model/describe_node/',								views.HorseIDBayesianNetworkAPI.describe_node.as_view()),
    url(r'^model/check_model/',									views.HorseIDBayesianNetworkAPI.check_model.as_view()),
    url(r'^model/get_edges/',                                   views.HorseIDBayesianNetworkAPI.get_edges.as_view()),
    url(r'^model/get_nodes/',                                   views.HorseIDBayesianNetworkAPI.get_nodes.as_view()),
    url(r'^model/get_cpds/',									views.HorseIDBayesianNetworkAPI.get_cpds.as_view()),
 	url(r'^model/get_cardinality/',								views.HorseIDBayesianNetworkAPI.get_cardinality.as_view()),
 	url(r'^model/get_local_independencies/',					views.HorseIDBayesianNetworkAPI.get_local_independencies.as_view()),
 	url(r'^model/get_active_trail_nodes/',						views.HorseIDBayesianNetworkAPI.get_active_trail_nodes.as_view()),
 	url(r'^model/query/',										views.HorseIDBayesianNetworkAPI.query.as_view()),
 	url(r'^model/map_query/',									views.HorseIDBayesianNetworkAPI.map_query.as_view()),
    url(r'^model/test_all/',                                    views.HorseIDBayesianNetworkAPI.test_all.as_view()),
    url(r'^$',                                                  TemplateView.as_view(template_name="index.html"),name='home'),
];

urlpatterns = format_suffix_patterns(urlpatterns);
