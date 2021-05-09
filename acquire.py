"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = ['ppatierno/formula1-telemetry-kafka',
 'NVIDIA-AI-IOT/Formula1Epoch',
 'jcnewell/ergast-f1-api',
 'SOYJUN/FTP-implement-based-on-UDP',
 'daz/live-f1',
 'izenecloud/sf1r-lite',
 'boostcamp-2020/Project15-C-Client-Based-Formula-Editor',
 'jonybur/f1-telemetry-client',
 'davidor/formula1-lap-charts',
 'rockt/ChemSpot',
 'boostcamp-2020/Project15-A-Client-Based-Formula-Editor',
 'ianperrin/MMM-Formula1',
 'F1Jobs/client',
 'billyct/happycalculator',
 'rothnic/formulapy',
 'TUMFTM/f1-timing-database',
 'bseddon/XBRL',
 'KurtMoran/F1-Data-Extractor',
 'boostcamp-2020/Project15-B-Client-Based-Formula-Editor',
 'sayantann11/all-classification-templetes-for-ML',
 'gareth/live-f1',
 'nlhans/SimTelemetry',
 'vkgnandhu177/Bayesian-Regression-and-Bitcoin',
 'dianaow/flask-react-d3-celery',
 'opensport/formula1.db',
 'gronberg/f1lt',
 'BlockchainLabs/SpreadCoin',
 'veronicanigro/Formula_1',
 'bacinger/f1-circuits',
 'jchannon/F1ES',
 'gionoa/Formula1API',
 'TimHanewich/Codemasters.F1_2020',
 'brombomb/f1info-alexa-skill',
 'SmCTwelve/f1-bot',
 'ppatierno/formula1-telemetry',
 'wearebraid/vue-formulate-i18n',
 'imartinezl/formula-one-viewer',
 'ahmedbera/f1lutter',
 'jewkesy/FormulaOne',
 'halldorstefans/McLarenAPI',
 'BatuhanYilmazzz/rn-formula-one-teams-slider',
 'gandalf1819/Formula1',
 'rhuangabrielsantos/Formula1-Backend',
 'ewa/802.11-data',
 'heerhaan/FormulaSim',
 'ashishpatel26/Machine-Learning-140-Formula',
 'rocketseat-experts-club/gerador-formularios-vuejs-2021-04-16',
 'YGersh/Year-1-Formulas',
 'geolessel/fantasy-f1-rules',
 'martijnvankekem/f1_telemetry_python',
 'tzai/rf-19-can-module',
 'cpoile/ExperimentServer',
 'Villanuevand/fanatico-f1',
 'paulhoad/gp2careditor',
 'LudemannEngineering/Formula-1000-Race-Car',
 'alejandrozambrana/Formula1-BBDD',
 'gionoa/FlatoutFormula1',
 'BlockchainLabs/Aeon',
 'junaidfarooqui/f1-standing-feeds',
 'DrDeath/phpBB3-F1-WebTipp',
 'WillSkywalker/nextf1race',
 'sim1/f1analytics',
 'thangpc/mhst2013-13-MathFormula',
 'arkraieski/formula1data',
 'rootmap/formula-cms-v1.2',
 'dcealopez/f1-alerts-telegram-bot',
 'LockeLamora/FridayCityLogic',
 'sayedafif/F1-Championship-Predictor',
 'maici95/f1-2020-telemetry',
 'mikethreels/formula1',
 'juliootonidev/Formula-de-Bhaskara',
 'tomredsky/f1db',
 'MartinCanovas/Formula1',
 'jaydsteele/f1telemetry',
 'PurplelinkPL/MIS-545-Project',
 'dianaow/Formula-1',
 'Sloopy3333/Formula-1-Prediction',
 'vkbansal/formula1-app',
 'carloscasciano/f1_standings_app',
 'ipshitag/knapsack0-1',
 'GuilhermeSAlves/nh',
 'DrDeath/phpbb-ext-f1webtip',
 'jon-wade/betfriend-mean',
 'hoangtnm/mark1_project',
 'samanthacardosoo/querys_f1',
 'Sigmus/marshalf1bot',
 'F1Vis/f1vis',
 'paulhoad/gp3careditor',
 'RJCodeAdvance/GUI-Modern-Parte-1-Formulario-Moderno-y-Plano-C-Sharp-y-WinForm',
 'andreivlad17/OpenGL_Formula1_mini-game',
 'steklopod/FormulaParser',
 'RyelBanfield/F1-Results-Scraper',
 'OliverHannover/Formula_1',
 'ministryofjustice/haproxy-formula',
 'majak96/grafika-formula-1',
 'brianvduong/Addition-Formulas',
 'brianvduong/Multiplication_Formulas',
 'DanielE0802/Formulario-1',
 'livef1/Livef1-web',
 'Dviejopomata/alexa-skill-f1',
 'dr0pdb/f1-cli',
 '3ximus/f12020-leaderboard',
 'isabelasousa1708/Formulario-html-1',
 'hbostann/pitwall',
 'cvqnguyen/formula_1_exploration',
 'dvdann/Tubes-tba',
 'ASURacingTeam/Formula-19-ICE',
 'jabbla/formular-parser',
 'cbaltingok98/Formula-1-Stats',
 'paulhoad/gp2objecteditor',
 's9v/CS402-Coursework1',
 'saunakc/TC18',
 'guiguitz/Nextion-STM32F103',
 'fedorn/lemur-4.11',
 '33H4B-544D4T/Merged-Calclator-v1.0',
 'viniciusthiengo/android-youtube-app-canal-formula-1',
 'kevin11h/2-Steps-Solution---Stability-Scalability---Fibonacci-Formula---Flower-Power',
 'leonardo-ono/JavaQuarternionRotatePointAroundAxisTest1',
 'mtlam/TempoPace',
 'emilstahl97/Envariabelanalys-SF1625',
 'FrancisBFTC/CFOCOL_Programming',
 'kayyali18/Formula-1-API',
 'saffeh6/blackmarket-script',
 'fattazzo/total-gp-world',
 'jfuerlinger/csharp_samples_ef_formula1-template',
 'shivammathur/homebrew-openssl-deprecated',
 'suryanshagarwal599/Crytpography-using-flask',
 'mlkasule/Geometry_N_Sided',
 'pointofsale/mongodb',
 'ickik/FormulaMath',
 'amccormick21/StratSim',
 'FreeeedomDive/F1Simulator',
 'jeffwh/reddit-formula1-stylehseet',
 'DavidLiuGit/pitlane',
 'zhendejianzheng1988/MFR100',
 'MightySameerDesai/Kidney-Exchange-by-Cycle-Formulation-v1-',
 'paulhoad/gp2trackeditor',
 'krivoj/FormulaD',
 'nickychow/formula',
 'Urbanov/F1Stats',
 'snives/F1-Media-Coverage-Analysis',
 'jigardave8/BMI-Calculator_swift5_iOS13',
 'jaylinski/kodi-addon-formula1',
 'renato76/formula1',
 'jbelien/F1-Circuits',
 'samatebintou1998/exercice_formulaire1',
 'prinetwo/formula1_SO1',
 'khanhhua/formula1',
 'andyvg/SFWF1League',
 'emerd01/Formula1',
 'jasmeen143/PROYECTO_M13',
 'Moszkowizz/Formula1',
 'alejandroayalamx/formulario1',
 'mnunes/Formula1',
 'licosan/Formula1',
 'RiosAlejandro/Formulario1',
 'quique-mandarina/formularioreactivo1',
 'Dariaaa/formula1',
 'gabriel-vga/formula1',
 'evefonwu/formula1-results',
 'bwobrien/formula1predictions',
 'evefonwu/formula1-admin',
 'rwoodley/FormulaToy_V2',
 'RavenHrafnagud/FormularioDeEncuestas',
 'Yors-git/formula1',
 'leandrocabral/formula1',
 'wfluit/Formula1',
 'jonathanfernandezfm/formula1-today',
 'Vilkku/reddit-formula1-stylesheet',
 'ozan-san/formula1_tester',
 'rwoodley/FormulaToy_V1',
 'alimoncul/Formula1Report',
 'igor1043/API-formula1',
 'piyush2468/Formula1-analysis',
 'Zellement/formula1gym',
 'ondergur/Formula1-Python',
 'mateuszpytlak/formula1-app',
 'ppatierno/codemotion-2021-formula1-kafka-camel',
 'QMIND-Team/Formula_1',
 'ppatierno/devconfcz-2021-formula1-kafka-streams',
 'jlsarabiac15/formulario-1',
 'gomon3/formulario',
 'story200/Formulario-1',
 'git-credential-1password/homebrew-git-credential-1password',
 'Dexterhutton45/formula-1',
 'icupeiro/project1-formulation',
 'Diegoireland1975/Alboreto27Rosso',
 'lciamp/formula_api',
 'sjuvonen/juanpablo',
 'renatinhotsw/logicaneppo',
 'ckomop0x/f1-seasons',
 'hugocorbucci/homebrew-elasticsearch15',
 'bennycwong/phoenix_f1_json_api',
 'NB28VT/F1Angular',
 'zigzagoog/formulastandings',
 'Darrellrp/Formula-1-App',
 'collectivecloudperu/validacion-formulario-angular10',
 'adampax/ergast-f1-openapi-doc',
 'Ireney/Formula-1-Picker-Game',
 'AriaTZY/auto_driving_f1',
 'IriniStivi/LF10-Formular',
 'rainbowturban/Formula-1-Race-Analysis',
 'anggiie/Formulaire-Inscription-1',
 'themallrat/formula-1-database',
 'luizgt/JavaFormula1',
 'ThomasHAOD/f1-stats-app-react',
 'alisonsi/apiFormula1',
 'carlosgeos/pit-stop-model',
 'NemanjaJakonic/Formula-F1-Stats',
 'RyanZurrin/Physics_Formula_Class1',
 'Oliver-Vandevelde/projet-1-formulaire',
 'ClaudeJanssenPro/projet-1-formulaire',
 'DragosBalmau/Formula-1-Arcade-Game',
 'manjunath5496/Resonance-Formula-Booklet-1',
 'martinbjeldbak/fonecal',
 'rpower/whatisformula1.com',
 'andersmh/fromula_master_app',
 'severinkaderli/Modul-133-Formularvalidierung',
 'wandealves/validacaoFormularioAngularJSParte1',
 'rootmap/Formula-cmsv1',
 'jubrito/Aula-11-Criando-formulario-django',
 'jamesomalley/f1-prediction-engine',
 'helderlim/formulario_php_versao0.1',
 'OpenThinkLabs/Tangent',
 'BieAnimaton/Formulario-Top-v1.0',
 'rabiaaydmr/Formula-1-Qualifier-Ranking-with-Linked-Lists-',
 'simon-kingston/2019-FIA-f1-World-Championship',
 'Jared-Chan/f1ml',
 'Peter-Win/charchem',
 'viniciusccarvalho/f1-kotlin',
 'cacoco/formulaic',
 'ScottHarrisonDev/F1-Data-Viz',
 'yucedincer/Visualization_Formula-1_RShiny_App',
 'landinezrichard/CSS3_Ejercicio12-Formularios',
 'bendrucker/1rm.js',
 'ExequielSchuster/F1DataAnalysis',
 'Simonvm9114/F1-weather-data',
 'marinavelosom/desafio1',
 'LuanMiqueias/f1-dashboard',
 'yts01/F1-Data-Analysis',
 'equistres/f1',
 'tugberkugurlu/f1-graph',
 'SmCTwelve/f1',
 'ZbonaL/CSCI3230_Final_Project',
 'mrgunior/A2B-Project',
 'Eternal-Monarch/URI-Online-Judge-1013-Altrernative-Solution-',
 'luiz-pereira/F1-Ruby-CLI-Project',
 'Eternal-Monarch/uri-problem-solved-1013',
 'RNGesus-exe/ROW_MAJOR_MATRIX_IN_1D',
 'jcmadsen/PacTire_Matlab',
 'hsayedi/Numerical-Analysis-Part-1',
 'bseddon/XBRL-tests',
 'daviddoret/RFin1',
 'engyii/f1-to-airtable',
 'emilstahl97/Multivariable-Calculus-SF1626',
 'guilhermeborgesbastos/anti-traversing-2d-array',
 'RubyHe-hub/B2B-Customized-Pricing-Optimization',
 'HoneyBeebus/loan_dolphins',
 'mark-sivill-splunk/F1-2020-Add-on-for-Splunk',
 'JoustingLion/joustinglion.github.io',
 'tylerengalla/kickstarter_analysis_challenge',
 'Mickeypeng/Chinese-paladin-1-composing-strategy',
 'Adammiszczak/photovoltaic-calculator',
 'jfuerlinger/csharp_samples_linq-formula1-template',
 'HZ-HBO-ICT/formula-1-part-2-start',
 'Scrirock/Exo-169-PHP-Send-mail-formulaire',
 'DamienOlivier567/Exo-158-PHP-Les-formulaires-nombres-aleatoires',
 'HZ-HBO-ICT/formula-1-start',
 'jrm-omg/ackerman-formulaire-brief19',
 'estacaohack9/104-formulario',
 'Scrirock/Exo-171-PHP-Les-fichiers-et-les-formulaires',
 'Scrirock/Exo-162-PHP-Formulaire-avec-select',
 'alessiobufano/2016-06-08-simulazione_Formula1_JDK11',
 'UrosKrampelj/Formula-1',
 'informatica-ieef-etsidi/formulas-aritmeticas-e105-ee105',
 'RyanWare1987/f1stats',
 'JackLJohnson/IFRS17',
 'cs107e/homebrew-cs107e',
 'bingfengding/formula',
 'this-is-project-x/Formula1-City-Website',
 'siempredelao/F1Kotlin',
 'CNR-IRSA-MEG/16S_normalization',
 'abdelouahidedd/Formulaire_1',
 'Victor-San/APP2000',
 'locknet11/Formula1',
 'MarlenCarmona/formulario2.1',
 'dfiaes/FormularioApp',
 'tjt69/Formula',
 'manjufy/f1',
 'RacingJack/F1',
 'mminute/hapiFormula1Api',
 'Bookoff/formula',
 'silentSp3cter/Formula1',
 'rahulpenumala95/formula1',
 'jmgiusti91/formulario1',
 'SchlankerMann/Formula1',
 'Aubacca/formulaOne',
 'kiw808/FORMULAIRE',
 'cristiangiuliani/formula1',
 'jrodrigue/formularioJS',
 'sshansravn/FormularApp',
 'fepe15/FormularioRegistro',
 'Juan-Garcia1/formula-1',
 'Nickbr/formula1_results',
 'ABS1019/f1',
 'm-migliore/throtl',
 'stevendnoble/formula1-2-3',
 'cnkndmr/formula1-data-analysis',
 'eboko1/F1',
 'FiveRedLights/f1-2017',
 'extraterrestria1/Formula1RaceResult',
 'mjuchli/f1-ticker-parser',
 'holokron/f1-almanac',
 'assis009/AtividadeSemaforo03',
 'janm2001/f1',
 'nathsimpson/f1-gql',
 'githabb/parseformula1',
 'fatihkiymet/formula-1',
 'Garoe/tactical-racer',
 'junynho2015/Formula-One',
 'quenandres/netF1',
 'xmanju/f1',
 'arnojong/f1',
 'beeprinz/startnow-react100-F1finder',
 'danilo-sds/formula-1',
 'BlueFish26/f1-stats',
 
]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)},"
            f" url: {url}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)