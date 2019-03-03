import numpy as np
from numpy import linalg as la
from math import log10
import scipy
from scipy import linalg


components = ['Microphone', 'Screen', 'FPU', 'LED0', 'LED1', 'Converter', 'Speaker', 'Buzzer', 'Microchip0',
              'Microchip1']
test_data = {
    'Test0': [('Screen', 0.09840709524367752), ('EnergyConsumed', 1.9902222818320978), ('LED0', 0.5537579627881133),
              ('Speaker', 0.23413712276700516), ('Converter', 0.8416645822828075), ('Microchip0', 0.27246025923506356),
              ('Microphone', 0.6912325037550041), ('Microchip1', 0.7806546842964981), ('Buzzer', 0.04959287550376734),
              ('FPU', 0.9035148171332333), ('LED1', 0.3073326586148679)],
    'Test1': [('Speaker', 0.7168330083539028), ('Screen', 0.7369653431791622), ('LED1', 0.9849028937848312),
              ('LED0', 0.6729760510228375), ('Microphone', 0.10673803271317583), ('Microchip0', 0.004934574240629819),
              ('EnergyConsumed', 1.4321429524016465), ('FPU', 0.5650104324553518), ('Buzzer', 0.7741413985599596),
              ('Converter', 0.4163858639918241), ('Microchip1', 0.4135845195394159)],
    'Test2': [('EnergyConsumed', 2.0559375423724275), ('FPU', 0.997270090225082), ('Screen', 0.9096409807634178),
              ('LED0', 0.31207740967108577), ('Converter', 0.16951406315981998), ('Speaker', 0.21030034452064816),
              ('Microphone', 0.9611065808330173), ('LED1', 0.21502236795686513), ('Microchip0', 0.7876208398264899),
              ('Microchip1', 0.4419914589255052), ('Buzzer', 0.5440630508985769)],
    'Test3': [('Microchip0', 0.36643544275874596), ('Converter', 0.0810808267296026), ('Speaker', 0.3233930300755443),
              ('LED0', 0.5113089119262774), ('Screen', 0.13503962182506057), ('Microphone', 0.7325951035577452),
              ('Microchip1', 0.6932590514966559), ('LED1', 0.7416155587060239), ('Buzzer', 0.9756350421965565),
              ('FPU', 0.9908265397175872), ('EnergyConsumed', 2.142105997582691)],
    'Test4': [('EnergyConsumed', 1.584408358948543), ('Microchip0', 0.19358701382500432), ('FPU', 0.5423021509470796),
              ('Microchip1', 0.5183404775768753), ('Converter', 0.18998700969281956),
              ('Microphone', 0.7094304374612235), ('LED1', 0.2781307069243021), ('Buzzer', 0.3202467131692719),
              ('Speaker', 0.0197559714957668), ('Screen', 0.9578338077779419), ('LED0', 0.4713217325953458)],
    'Test5': [('FPU', 0.6742272255290204), ('LED0', 0.7167771801028261), ('Converter', 0.8309142003939775),
              ('Microchip1', 0.8692644290078414), ('Screen', 0.48490479027132627), ('Microphone', 0.20457883428409773),
              ('Speaker', 0.6679520050963801), ('LED1', 0.6908457562320122), ('Buzzer', 0.25792063247117614),
              ('EnergyConsumed', 1.894728009322498), ('Microchip0', 0.4156974342357712)],
    'Test6': [('LED1', 0.7489491847552509), ('FPU', 0.9840315503053534), ('EnergyConsumed', 2.0059071828739974),
              ('LED0', 0.42933401479663336), ('Converter', 0.15674622400987825), ('Microchip1', 0.6554116444626874),
              ('Microchip0', 0.9211576305070767), ('Screen', 0.08306202133151108), ('Speaker', 0.06709358956898592),
              ('Microphone', 0.4262955712811143), ('Buzzer', 0.8953895467198086)],
    'Test7': [('EnergyConsumed', 1.3771425388445118), ('Screen', 0.06325531110053062),
              ('Microchip0', 0.5128772047504002), ('Buzzer', 0.8914943901575896), ('Microchip1', 0.2399352773620982),
              ('LED0', 0.42412769102509496), ('Microphone', 0.11818776888374438), ('Converter', 0.8264032907686883),
              ('LED1', 0.17888563946595648), ('Speaker', 0.35732335353760925), ('FPU', 0.8203329182710452)],
    'Test8': [('FPU', 0.35859309455352384), ('Microchip0', 0.4504653320544838), ('Converter', 0.6426329422852921),
              ('LED1', 0.4296149001681946), ('Microchip1', 0.9158290398151469), ('EnergyConsumed', 2.271834789567588),
              ('Speaker', 0.5805326293082245), ('Microphone', 0.51010023645503), ('LED0', 0.9850521766782204),
              ('Buzzer', 0.9200896900216144), ('Screen', 0.6735338157207172)],
    'Test9': [('Microchip0', 0.17263264858339566), ('Speaker', 0.6473247892965333), ('Screen', 0.35251006371610116),
              ('Converter', 0.4189457936339056), ('Buzzer', 0.367078084159138), ('LED1', 0.1648840179133051),
              ('FPU', 0.2305120705761292), ('EnergyConsumed', 1.0105598319295905), ('Microchip1', 0.14576654027927272),
              ('Microphone', 0.3702543741867734), ('LED0', 0.5010677281906357)]}

matrix = []
x = []
for _, test in test_data.items():
    row = []
    test_dict = dict(test)
    for c in components:
        if c != "EnergyConsumed":
            row.append(test_dict[c])
    x.append(test_dict["EnergyConsumed"])
    matrix.append(row)

# for row in matrix:
#     print(row)
matrix = np.array(matrix)
x = np.array(x).T

power_usage = la.solve(matrix,x)
print(power_usage)
# compos = []
# energy = []
# print(components)
# print(test_data['Test0'])
# for test in test_data.values():
#     compo = []
#     test_dict = dict(test)
#     for component in components:
#         if component == "EnergyConsumed":
#             continue
#         compo.append(test_dict[component])
#     compos.append(compo)
#     energy.append(test_dict['EnergyConsumed'])
# compos = np.array(compos)
# energy = np.array(energy)
# power_usage = solve(compos, energy)
