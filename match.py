import csv
import pandas as pd
import numpy as np
import argparse

def match(dis1, dis2):
    diseases = ["Exposure to forces of nature","Environmental heat and cold exposure","Ebola","Conflict and terrorism","Typhoid and paratyphoid","Other malignant neoplasms","Other cardiovascular and circulatory diseases","Invasive Non-typhoidal Salmonella (iNTS)","Whooping cough","Tetanus","Measles","Varicella and herpes zoster","Malaria","Chagas disease","Leishmaniasis","Protein-energy malnutrition","Iodine deficiency","Vitamin A deficiency","Dietary iron deficiency","Other nutritional deficiencies","Sexually transmitted infections excluding HIV","Tuberculosis","HIV/AIDS","Diarrheal diseases","Other intestinal infectious diseases","Lower respiratory infections","Upper respiratory infections","Otitis media","Meningitis","Encephalitis","Appendicitis","Paralytic ileus and intestinal obstruction","Inguinal, femoral, and abdominal hernia","Inflammatory bowel disease","Endocrine, metabolic, blood and immune disorders","Rheumatoid arthritis","Osteoarthritis","Low back pain","Neck pain","African trypanosomiasis","Schistosomiasis","Cysticercosis","Cystic echinococcosis","Lymphatic filariasis","Onchocerciasis","Trachoma","Dengue","Yellow fever","Lip and oral cavity cancer","Nasopharynx cancer","Other pharynx cancer","Gallbladder and biliary tract cancer","Pancreatic cancer","Malignant skin melanoma","Other digestive diseases","Alzheimer's disease and other dementias","Parkinson's disease","Idiopathic epilepsy","Multiple sclerosis","Motor neuron disease","Other neurological disorders","Schizophrenia","Drug use disorders","Depressive disorders","Bipolar disorder","Anxiety disorders","Eating disorders","Viral skin diseases","Acne vulgaris","Pancreatitis","Other musculoskeletal disorders","Congenital birth defects","Other mental disorders","Diabetes mellitus","Acute glomerulonephritis","Chronic kidney disease","Urinary diseases and male infertility","Gynecological diseases","Other unintentional injuries","Self-harm","Interpersonal violence","Food-borne trematodiases","Other neglected tropical diseases","Road injuries","Other transport injuries","Falls","Drowning","Fire, heat, and hot substances","Poisonings","Gout","Diphtheria","Stomach cancer","Liver cancer","Larynx cancer","Tracheal, bronchus and lung cancer","Breast cancer","Cervical cancer","Uterine cancer","Prostate cancer","Non-melanoma skin cancer","Ovarian cancer","Testicular cancer","Kidney cancer","Bladder cancer","Brain and central nervous system cancer","Thyroid cancer","Mesothelioma","Hodgkin lymphoma","Non-Hodgkin lymphoma","Multiple myeloma","Leukemia","Dermatitis","Psoriasis","Scabies","Fungal skin diseases","Alopecia areata","Pruritus","Non-rheumatic valvular heart disease","Chronic obstructive pulmonary disease","Pneumoconiosis","Asthma","Interstitial lung disease and pulmonary sarcoidosis","Other chronic respiratory diseases","Cirrhosis and other chronic liver diseases","Urticaria","Decubitus ulcer","Other skin and subcutaneous diseases","Age-related and other hearing loss","Other sense organ diseases","Oral disorders","Colon and rectum cancer","Rabies","Intestinal nematode infections","Maternal disorders","Neonatal disorders","Autism spectrum disorders","Attention-deficit/hyperactivity disorder","Conduct disorder","Idiopathic developmental intellectual disability","Exposure to mechanical forces","Headache disorders","Acute hepatitis","Leprosy","Other unspecified infectious diseases","Esophageal cancer","Adverse effects of medical treatment","Animal contact","Other neoplasms","Rheumatic heart disease","Ischemic heart disease","Stroke","Hypertensive heart disease","Executions and police conflict","Zika virus","Guinea worm disease","Hemoglobinopathies and hemolytic anemias","Alcohol use disorders","Sudden infant death syndrome","Bacterial skin diseases","Blindness and vision loss","Upper digestive system diseases","Vascular intestinal disorders","Gallbladder and biliary diseases","Peripheral artery disease","Endocarditis","Cardiomyopathy and myocarditis","Atrial fibrillation and flutter","Aortic aneurysm","Foreign body"]
    countries = ["Cambodia","Armenia","Philippines","Tajikistan","Georgia","Lao People's Democratic Republic","Maldives","Kyrgyzstan","Albania","Uzbekistan","Poland","Fiji","Bulgaria","Brunei Darussalam","North Macedonia","Czechia","Viet Nam","Barbados","Trinidad and Tobago","Israel","Jamaica","Thailand","Saint Vincent and the Grenadines","Serbia","Germany","Dominican Republic","Guyana","Belarus","Austria","Cuba","Bolivia (Plurinational State of)","Finland","Antigua and Barbuda","Chile","Marshall Islands","Slovenia","Solomon Islands","Iceland","Cyprus","Paraguay","Papua New Guinea","Colombia","Republic of Moldova","Latvia","Peru","Netherlands","Democratic People's Republic of Korea","Vanuatu","China","United States of America","El Salvador","Luxembourg","Republic of Korea","Bahrain","Portugal","Myanmar","Indonesia","Honduras","Ukraine","Sweden","Iran (Islamic Republic of)","United Kingdom","Azerbaijan","Morocco","Brazil","Venezuela (Bolivarian Republic of)","New Zealand","Mongolia","Canada","Tunisia","Croatia","Turkmenistan","Andorra","Bosnia and Herzegovina","United Arab Emirates","Argentina","Suriname","Jordan","Nicaragua","Lebanon","Oman","India","Malaysia","Saudi Arabia","Dominica","Kazakhstan","Bangladesh","Hungary","Haiti","Italy","Greece","Romania","Denmark","Kiribati","France","Slovakia","Saint Lucia","Algeria","Ireland","Montenegro","Uruguay","Belgium","Australia","Grenada","Pakistan","Sri Lanka","Costa Rica","Belize","Tonga","Comoros","Bahamas","Timor-Leste","Samoa","Micronesia (Federated States of)","Lithuania","Mauritania","Afghanistan","Liberia","Chad","Taiwan (Province of China)","Norway","Japan","Eritrea","Estonia","Ecuador","Guinea","Nigeria","Cameroon","Gambia","Benin","Russian Federation","Malta","Spain","Kenya","Togo","Guatemala","Senegal","Central African Republic","Singapore","Botswana","Palestine","Syrian Arab Republic","Mexico","Switzerland","Egypt","Mozambique","Kuwait","American Samoa","Qatar","United Republic of Tanzania","Bhutan","Burundi","Iraq","Panama","Malawi","Libya","Zambia","Yemen","Seychelles","Namibia","Turkey","Gabon","Democratic Republic of the Congo","Eswatini","Angola","Nepal","Djibouti","Guinea-Bissau","Niger","Sierra Leone","Burkina Faso","Lesotho","C?te d'Ivoire","Cabo Verde","Madagascar","Ethiopia","Mali","Sao Tome and Principe","Mauritius","South Africa","Congo","Zimbabwe","Somalia","Tuvalu","Puerto Rico","Equatorial Guinea","Cook Islands","Guam","Bermuda","South Sudan","Monaco","Ghana","Uganda","Northern Mariana Islands","Rwanda","San Marino","Nauru","Sudan","Tokelau","Greenland","Niue","Palau","Saint Kitts and Nevis","United States Virgin Islands"]
    with open("top29.csv", mode="rt", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        row1 = []
        row2 = []
        country = []
        for i,rows in enumerate(reader):
            if diseases[i] == dis1:
                row1 = rows
            if diseases[i] == dis2:
                row2 = rows
        sum = 0
        for i in range(204):
            if row1[''''''+str(i)+''''''] == '1' and row2[''''''+str(i)+''''''] == '1':
                sum+=1
                country.append(countries[i])
    print("'{}' and '{}' similarity is {:.2f} %".format(dis1, dis2, sum * 100/29.0))
    print("Their top similar countries:")
    for i in country:
        print(i)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='disease1 and disease2')

    parser.add_argument('--dis1', dest='dis1', default="Eating disorders", type=str, help='Name of the first disease')

    parser.add_argument('--dis2', dest='dis2', default="Parkinson's disease", type=str, help='Name of the second disease')

    args = parser.parse_args()

    match(args.dis1, args.dis2)
    # example1: python match.py --dis1 "Eating disorders" --dis2 "Parkinson's disease"
    # example2: python match.py --dis1 "Asthma" --dis2 "Bladder cancer"

