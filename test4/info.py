import yaml
from flask import Flask, render_template
app=Flask(__name__)

stream=open("data.yaml",'r') #lire les données
docs=yaml.load(stream)
docs=dict(docs)                 #transformer les données en dictionnaire
docs_keys=list(docs.keys())
doc_keys_0=docs_keys[0]         #hostname
doc_keys_1=docs_keys[1]         #ip
doc_keys_2=docs_keys[2]         #snmp
doc_keys_3=docs_keys[3]         #vlans

docs_values=list(docs.values())
doc_values_0=docs_values[0]         #testswitch
doc_values_1=docs_values[1]         #10.101.0.221

values_snmp=docs_values[2]          #dictionnaire snmp
snmp_keys=list(values_snmp.keys())              #keys de snmp
snmp_values=list(values_snmp.values())          #valeurs de snmp

snmp_keys_0=snmp_keys[0]
snmp_keys_1=snmp_keys[1]
snmp_keys_2=snmp_keys[2]
snmp_keys_3=snmp_keys[3]
snmp_keys_4=snmp_keys[4]

snmp_values_0=snmp_values[0]
snmp_values_1=snmp_values[1]
snmp_values_2=snmp_values[2]
snmp_values_3=snmp_values[3]

snmp_trap=values_snmp[snmp_keys_4]                  #la dernière valeur de snmp est un dictionnaire: trap
snmp_trap_0=snmp_trap[0]                            #pour obtenir les keys
snmp_keys_key=snmp_trap_0.keys()
snmp_4_key=list(snmp_keys_key)[0]

snmp_4_value0=list(snmp_trap_0.values())            #la première valeur de snmp_trap
snmp_4_value0=snmp_4_value0[0]

snmp_trap_1=snmp_trap[1]                            #la deuxième valeur de snmp_trap
snmp_4_value1=list(snmp_trap_1.values())
snmp_4_value1=snmp_4_value1[0]

snmp_trap_2=snmp_trap[2]                               #la troisième valeur de snmp_trap
snmp_4_value2=list(snmp_trap_2.values())
snmp_4_value2=snmp_4_value2[0]

docs_3_value1=docs[doc_keys_3][0]                       #vlan dictionnaire
doc_vlan_keys=list(docs_3_value1.keys())                #les keys de vlan dictionnaire

vlan_dics=list(docs[docs_keys[3]])                      #les valeurs de vlan dictionnaire
vlan_values0=list(vlan_dics[0].values())
vlan_values1=list(vlan_dics[1].values())
vlan_values2=list(vlan_dics[2].values())
vlan_values3=list(vlan_dics[3].values())



@app.route('/')
def home():
    return render_template('home.html',key0=doc_keys_0,key1=doc_keys_1,key2=doc_keys_2,key3=doc_keys_3,
                           values0=doc_values_0,values1=doc_values_1,
                           snmp_keys_0=snmp_keys_0,snmp_keys_1=snmp_keys_1,snmp_keys_2=snmp_keys_2,snmp_keys_3=snmp_keys_3,snmp_keys_4=snmp_keys_4,snmp_4_key=snmp_4_key,
                           snmp_values_0=snmp_values_0,snmp_values_1=snmp_values_1,snmp_values_2=snmp_values_2,snmp_values_3=snmp_values_3,
                           snmp_4_value0=snmp_4_value0,snmp_4_value1=snmp_4_value1,snmp_4_value2=snmp_4_value2,
                           doc_vlan_keys=doc_vlan_keys,
                           vlan_values0=vlan_values0,vlan_values1=vlan_values1,vlan_values2=vlan_values2,vlan_values3=vlan_values3)

if __name__=='__main__':
    app.run(debug=True)