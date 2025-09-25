import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class PSFinanceAnalyzer:
    def __init__(self):
        self.parti = "Parti Socialiste (PS)"
        self.colors = ['#FF0000', '#FF6600', '#FF9999', '#CC0000', '#FF3333', 
                      '#990000', '#FF3366', '#FFCCCC', '#FF6666', '#CC6666']
        
        self.start_year = 1971  # Congrès d'Epinay - création du PS moderne
        self.end_year = 2025
        self.creation_year = 1971
        self.presidential_years = [1974, 1981, 1988, 1995, 2002, 2007, 2012, 2017, 2022]
        
        # Configuration spécifique au PS
        self.config = {
            "type": "parti_politique",
            "orientation": "gauche_gouvernementale",
            "electorat_cible": ["ouvriers", "employes", "enseignants", "fonctionnaires", "classes_moyennes"],
            "budget_base": 20,  # millions d'euros (historiquement important)
            "adherents_base": 100000,
            "importance": "historique",
            "sources_financement": ["cotisations", "dons", "financement_public", "evenements", "elus"]
        }
        
    def generate_financial_data(self):
        """Génère des données financières pour le PS"""
        print(f"🏛️ Génération des données financières pour {self.parti}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données d'adhérents et structure
        data['Adherents'] = self._simulate_adherents(dates)
        data['Federations_Departementales'] = self._simulate_federations(dates)
        data['Elus_Locaux'] = self._simulate_elus_locaux(dates)
        data['Elus_Nationaux'] = self._simulate_elus_nationaux(dates)
        data['Maires'] = self._simulate_maires(dates)
        data['Conseillers_Regionaux'] = self._simulate_conseillers_regionaux(dates)
        
        # Revenus du parti
        data['Revenus_Total'] = self._simulate_total_revenue(dates)
        data['Cotisations_Adherents'] = self._simulate_membership_fees(dates)
        data['Dons_Prives'] = self._simulate_private_donations(dates)
        data['Financement_Public'] = self._simulate_public_funding(dates)
        data['Revenus_Evenements'] = self._simulate_event_revenue(dates)
        data['Cotisations_Elus'] = self._simulate_elected_officials_fees(dates)
        data['Revenus_Formations'] = self._simulate_training_revenue(dates)
        
        # Dépenses du parti
        data['Depenses_Total'] = self._simulate_total_expenses(dates)
        data['Depenses_Personnel'] = self._simulate_staff_expenses(dates)
        data['Depenses_Campagnes'] = self._simulate_campaign_expenses(dates)
        data['Depenses_Communication'] = self._simulate_communication_expenses(dates)
        data['Depenses_Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Depenses_Formation'] = self._simulate_training_expenses(dates)
        data['Depenses_International'] = self._simulate_international_expenses(dates)
        
        # Indicateurs financiers
        data['Taux_Execution_Budget'] = self._simulate_budget_execution_rate(dates)
        data['Ratio_Cotisations_Revenus'] = self._simulate_membership_ratio(dates)
        data['Dependance_Financement_Public'] = self._simulate_public_funding_dependency(dates)
        data['Solde_Financier'] = self._simulate_financial_balance(dates)
        data['Endettement'] = self._simulate_debt(dates)
        
        # Investissements stratégiques
        data['Investissement_Communication'] = self._simulate_communication_investment(dates)
        data['Investissement_Numérique'] = self._simulate_digital_investment(dates)
        data['Investissement_Formation'] = self._simulate_training_investment(dates)
        data['Investissement_Recherche'] = self._simulate_research_investment(dates)
        data['Investissement_International'] = self._simulate_international_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques au PS
        self._add_party_trends(df)
        
        return df
    
    def _simulate_adherents(self, dates):
        """Simule le nombre d'adhérents"""
        base_adherents = self.config["adherents_base"]
        
        adherents = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution historique des adhérents selon les périodes politiques
            if 1971 <= year <= 1981:  # Montée vers le pouvoir
                growth_rate = 0.12
            elif 1981 <= year <= 1988:  # Présidence Mitterrand
                growth_rate = 0.08
            elif 1988 <= year <= 1995:  # Second septennat
                growth_rate = 0.02
            elif 1995 <= year <= 2002:  # Opposition
                growth_rate = -0.05
            elif 2002 <= year <= 2012:  # Reconstruction et victoire
                growth_rate = 0.10
            elif 2012 <= year <= 2017:  # Présidence Hollande
                growth_rate = -0.08
            elif 2017 <= year <= 2022:  # Effondrement
                growth_rate = -0.25
            else:  # 2023-2025 - Reconstruction
                growth_rate = 0.03
                
            growth = 1 + growth_rate * (i/10)
            noise = np.random.normal(1, 0.07)
            adherents.append(base_adherents * growth * noise)
        
        return adherents
    
    def _simulate_federations(self, dates):
        """Simule le nombre de fédérations départementales"""
        base_federations = 100  # Métropole + outre-mer
        
        federations = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                growth_rate = 0.03
            elif year <= 2010:
                growth_rate = 0.01
            else:
                growth_rate = -0.01
                
            growth = 1 + growth_rate * (i/15)
            federations.append(base_federations * growth)
        
        return federations
    
    def _simulate_elus_locaux(self, dates):
        """Simule le nombre d'élus locaux"""
        base_elus = 30000
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections municipales
            if year in [1971, 1977, 1983, 1989, 1995, 2001, 2008, 2014, 2020]:
                if year <= 1995:
                    multiplier = 1.2
                elif year <= 2014:
                    multiplier = 1.1
                else:
                    multiplier = 0.8
            else:
                multiplier = 1.0
                
            # Tendance générale
            if year <= 1990:
                growth_rate = 0.04
            elif year <= 2010:
                growth_rate = 0.01
            else:
                growth_rate = -0.03
                
            growth = 1 + growth_rate * (i/20)
            noise = np.random.normal(1, 0.05)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_elus_nationaux(self, dates):
        """Simule le nombre d'élus nationaux"""
        base_elus = 200
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections législatives
            if year in [1973, 1978, 1981, 1986, 1988, 1993, 1997, 2002, 2007, 2012, 2017, 2022]:
                if year in [1981, 1988, 1997, 2012]:  # Victoires
                    multiplier = 1.8
                elif year in [1978, 1993, 2002, 2007, 2017]:  # Défaites
                    multiplier = 0.6
                else:
                    multiplier = 1.2
            else:
                multiplier = 1.0
                
            growth = 1 - 0.01 * (i/10)
            noise = np.random.normal(1, 0.10)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_maires(self, dates):
        """Simule le nombre de maires PS"""
        base_maires = 500
        
        maires = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1995:
                growth_rate = 0.05
            elif year <= 2014:
                growth_rate = 0.02
            else:
                growth_rate = -0.04
                
            growth = 1 + growth_rate * (i/15)
            noise = np.random.normal(1, 0.08)
            maires.append(base_maires * growth * noise)
        
        return maires
    
    def _simulate_conseillers_regionaux(self, dates):
        """Simule le nombre de conseillers régionaux"""
        base_conseillers = 300
        
        conseillers = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1986:  # Premières régionales
                if year <= 1998:
                    growth_rate = 0.08
                elif year <= 2010:
                    growth_rate = 0.03
                else:
                    growth_rate = -0.05
            else:
                growth_rate = 0
                
            growth = 1 + growth_rate * max(0, (year - 1986)/20)
            noise = np.random.normal(1, 0.09)
            conseillers.append(base_conseillers * growth * noise if year >= 1986 else 0)
        
        return conseillers
    
    def _simulate_total_revenue(self, dates):
        """Simule les revenus totaux"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Croissance historique des revenus
            if 1971 <= year <= 1981:  # Montée vers le pouvoir
                growth_rate = 0.15
            elif 1981 <= year <= 1995:  # Au pouvoir
                growth_rate = 0.10
            elif 1995 <= year <= 2002:  # Opposition
                growth_rate = -0.03
            elif 2002 <= year <= 2012:  # Reconstruction
                growth_rate = 0.08
            elif 2012 <= year <= 2017:  # Au pouvoir
                growth_rate = 0.05
            elif 2017 <= year <= 2022:  # Effondrement
                growth_rate = -0.20
            else:  # Reconstruction
                growth_rate = 0.02
                
            growth = 1 + growth_rate * (i/15)
            noise = np.random.normal(1, 0.08)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_membership_fees(self, dates):
        """Simule les cotisations des adhérents"""
        base_fees = self.config["budget_base"] * 0.20
        
        fees = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1981:
                growth_rate = 0.12
            elif year <= 1995:
                growth_rate = 0.05
            elif year <= 2012:
                growth_rate = 0.03
            else:
                growth_rate = -0.08
                
            growth = 1 + growth_rate * (i/12)
            noise = np.random.normal(1, 0.06)
            fees.append(base_fees * growth * noise)
        
        return fees
    
    def _simulate_private_donations(self, dates):
        """Simule les dons privés"""
        base_donations = self.config["budget_base"] * 0.25
        
        donations = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution législative et politique
            if year <= 1990:  # Peu de réglementation
                multiplier = 1.3
            elif year <= 2010:  # Réglementation renforcée
                multiplier = 0.9
            else:  # Contrôles stricts
                multiplier = 0.7
                
            # Cycles électoraux
            if year in self.presidential_years:
                electoral_multiplier = 1.6
            else:
                electoral_multiplier = 1.0
                
            growth = 1 + 0.02 * (i/10)
            noise = np.random.normal(1, 0.12)
            donations.append(base_donations * growth * multiplier * electoral_multiplier * noise)
        
        return donations
    
    def _simulate_public_funding(self, dates):
        """Simule le financement public"""
        base_funding = self.config["budget_base"] * 0.35
        
        funding = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Dépend des résultats électoraux
            if year in [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,  # Mitterrand
                       1997, 1998, 1999, 2000, 2001, 2002,  # Jospin
                       2012, 2013, 2014, 2015, 2016, 2017]:  # Hollande
                multiplier = 1.5
            else:
                multiplier = 0.8
                
            growth = 1 + 0.03 * (i/10)
            noise = np.random.normal(1, 0.07)
            funding.append(base_funding * growth * multiplier * noise)
        
        return funding
    
    def _simulate_event_revenue(self, dates):
        """Simule les revenus des événements"""
        base_revenue = self.config["budget_base"] * 0.08
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Universités d'été, congrès, etc.
            if year in [1971, 1974, 1981, 1988, 1995, 2002, 2008, 2012, 2017, 2022]:
                multiplier = 1.8  # Années de congrès importants
            else:
                multiplier = 1.0
                
            growth = 1 + 0.02 * (i/10)
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * multiplier * noise)
        
        return revenue
    
    def _simulate_elected_officials_fees(self, dates):
        """Simule les cotisations des élus"""
        base_fees = self.config["budget_base"] * 0.10
        
        fees = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2000:
                growth_rate = 0.05
            elif year <= 2015:
                growth_rate = 0.02
            else:
                growth_rate = -0.06
                
            growth = 1 + growth_rate * max(0, (year - 1971)/30)
            noise = np.random.normal(1, 0.08)
            fees.append(base_fees * growth * noise)
        
        return fees
    
    def _simulate_training_revenue(self, dates):
        """Simule les revenus des formations"""
        base_revenue = self.config["budget_base"] * 0.02
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1990:  # Développement de l'offre de formation
                growth = 1 + 0.04 * max(0, (year - 1990)/20)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.09)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.95
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in self.presidential_years:  # Années électorales
                multiplier = 1.5
            else:
                multiplier = 1.0
                
            growth = 1 + 0.04 * (i/10)
            noise = np.random.normal(1, 0.07)
            expenses.append(base_expenses * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_staff_expenses(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = self.config["budget_base"] * 0.40  # Structure importante
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                growth_rate = 0.06
            elif year <= 2010:
                growth_rate = 0.03
            else:  # Rationalisation
                growth_rate = -0.04
                
            growth = 1 + growth_rate * (i/12)
            noise = np.random.normal(1, 0.05)
            expenses.append(base_staff * growth * noise)
        
        return expenses
    
    def _simulate_campaign_expenses(self, dates):
        """Simule les dépenses de campagne"""
        base_campaign = self.config["budget_base"] * 0.20
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in self.presidential_years:  # Années électorales
                multiplier = 2.5
            elif year in [y-1 for y in self.presidential_years]:  # Années pré-électorales
                multiplier = 1.5
            else:
                multiplier = 0.7
                
            growth = 1 + 0.03 * (i/10)
            noise = np.random.normal(1, 0.15)
            expenses.append(base_campaign * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_communication_expenses(self, dates):
        """Simule les dépenses de communication"""
        base_communication = self.config["budget_base"] * 0.12
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1990:  # Importance croissante de la communication
                growth = 1 + 0.06 * max(0, (year - 1990)/20)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.10)
            expenses.append(base_communication * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = self.config["budget_base"] * 0.15
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            growth = 1 + 0.02 * (i/10)
            noise = np.random.normal(1, 0.04)
            expenses.append(base_operating * growth * noise)
        
        return expenses
    
    def _simulate_training_expenses(self, dates):
        """Simule les dépenses de formation"""
        base_training = self.config["budget_base"] * 0.05
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1980:  # Développement de l'offre de formation
                growth = 1 + 0.04 * max(0, (year - 1980)/30)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.08)
            expenses.append(base_training * growth * noise)
        
        return expenses
    
    def _simulate_international_expenses(self, dates):
        """Simule les dépenses internationales"""
        base_international = self.config["budget_base"] * 0.03
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1975:  # Engagement international
                growth = 1 + 0.03 * max(0, (year - 1975)/30)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.12)
            expenses.append(base_international * growth * noise)
        
        return expenses
    
    def _simulate_budget_execution_rate(self, dates):
        """Simule le taux d'exécution du budget"""
        rates = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1980:
                base_rate = 0.82
            elif year <= 2000:
                base_rate = 0.85
            elif year <= 2015:
                base_rate = 0.88
            else:  # Difficultés financières
                base_rate = 0.80
                
            noise = np.random.normal(1, 0.05)
            rates.append(base_rate * noise)
        
        return rates
    
    def _simulate_membership_ratio(self, dates):
        """Simule le ratio cotisations/revenus"""
        ratios = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1980:
                base_ratio = 0.25
            elif year <= 2000:
                base_ratio = 0.22
            elif year <= 2015:
                base_ratio = 0.18
            else:  # Baisse de la part des cotisations
                base_ratio = 0.12
                
            noise = np.random.normal(1, 0.06)
            ratios.append(base_ratio * noise)
        
        return ratios
    
    def _simulate_public_funding_dependency(self, dates):
        """Simule la dépendance au financement public"""
        dependencies = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1990:
                base_dependency = 0.30
            elif year <= 2010:
                base_dependency = 0.40
            else:  # Plus dépendant
                base_dependency = 0.50
                
            noise = np.random.normal(1, 0.07)
            dependencies.append(base_dependency * noise)
        
        return dependencies
    
    def _simulate_financial_balance(self, dates):
        """Simule le solde financier"""
        balances = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in self.presidential_years:  # Déficits électoraux
                base_balance = -0.10
            elif year in [y+1 for y in self.presidential_years]:  # Redressement
                base_balance = 0.05
            else:
                base_balance = 0.02
                
            noise = np.random.normal(1, 0.08)
            balances.append(base_balance * noise)
        
        return balances
    
    def _simulate_debt(self, dates):
        """Simule l'endettement"""
        base_debt = self.config["budget_base"] * 0.3
        
        debt = []
        current_debt = base_debt
        for i, date in enumerate(dates):
            year = date.year
            
            if year in self.presidential_years:  # Augmentation dette
                change_rate = 0.15
            elif year in [y+1 for y in self.presidential_years]:  # Réduction dette
                change_rate = -0.08
            else:
                change_rate = 0.03
                
            current_debt *= (1 + change_rate)
            noise = np.random.normal(1, 0.06)
            debt.append(current_debt * noise)
        
        return debt
    
    def _simulate_communication_investment(self, dates):
        """Simule l'investissement en communication"""
        base_investment = self.config["budget_base"] * 0.07
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1990:
                growth = 1 + 0.05 * max(0, (year - 1990)/20)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.11)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_digital_investment(self, dates):
        """Simule l'investissement numérique"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2000:
                growth = 1 + 0.10 * max(0, (year - 2000)/15)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_training_investment(self, dates):
        """Simule l'investissement en formation"""
        base_investment = self.config["budget_base"] * 0.05
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1980:
                growth = 1 + 0.04 * max(0, (year - 1980)/30)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.10)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_research_investment(self, dates):
        """Simule l'investissement en recherche"""
        base_investment = self.config["budget_base"] * 0.03
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1990:
                growth = 1 + 0.03 * max(0, (year - 1990)/20)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.12)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_international_investment(self, dates):
        """Simule l'investissement international"""
        base_investment = self.config["budget_base"] * 0.02
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1975:
                growth = 1 + 0.02 * max(0, (year - 1975)/30)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _add_party_trends(self, df):
        """Ajoute des tendances réalistes pour le PS"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Congrès d'Epinay (1971)
            if year == 1971:
                df.loc[i, 'Revenus_Total'] *= 1.5
                df.loc[i, 'Adherents'] *= 2.0
            
            # Élection de Mitterrand (1981)
            if year == 1981:
                df.loc[i, 'Revenus_Total'] *= 1.8
                df.loc[i, 'Financement_Public'] *= 2.2
                df.loc[i, 'Elus_Nationaux'] *= 2.5
            
            # Réélection de Mitterrand (1988)
            if year == 1988:
                df.loc[i, 'Revenus_Total'] *= 1.3
                df.loc[i, 'Dons_Prives'] *= 1.6
            
            # Victoire de la gauche plurielle (1997)
            if year == 1997:
                df.loc[i, 'Financement_Public'] *= 1.4
                df.loc[i, 'Elus_Nationaux'] *= 1.8
            
            # Défaite de Jospin (2002)
            if year == 2002:
                df.loc[i, 'Adherents'] *= 0.85
                df.loc[i, 'Financement_Public'] *= 0.75
            
            # Défaite de Royal (2007)
            if year == 2007:
                df.loc[i, 'Adherents'] *= 0.90
                df.loc[i, 'Revenus_Total'] *= 0.95
            
            # Élection de Hollande (2012)
            if year == 2012:
                df.loc[i, 'Revenus_Total'] *= 1.4
                df.loc[i, 'Financement_Public'] *= 1.6
                df.loc[i, 'Elus_Nationaux'] *= 1.7
            
            # Défaite de Hamon (2017)
            if year == 2017:
                df.loc[i, 'Adherents'] *= 0.60
                df.loc[i, 'Revenus_Total'] *= 0.55
                df.loc[i, 'Financement_Public'] *= 0.40
                df.loc[i, 'Elus_Nationaux'] *= 0.30
            
            # Primaires 2022
            if year == 2022:
                df.loc[i, 'Depenses_Campagnes'] *= 1.4
                df.loc[i, 'Investissement_Communication'] *= 1.3
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances du PS"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des revenus et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des revenus
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Adhérents et structure
        ax4 = plt.subplot(4, 2, 4)
        self._plot_membership_structure(df, ax4)
        
        # 5. Investissements stratégiques
        ax5 = plt.subplot(4, 2, 5)
        self._plot_strategic_investments(df, ax5)
        
        # 6. Indicateurs financiers
        ax6 = plt.subplot(4, 2, 6)
        self._plot_financial_indicators(df, ax6)
        
        # 7. Évolution des élus
        ax7 = plt.subplot(4, 2, 7)
        self._plot_elected_officials(df, ax7)
        
        # 8. Situation financière
        ax8 = plt.subplot(4, 2, 8)
        self._plot_financial_situation(df, ax8)
        
        plt.suptitle(f'Analyse des Finances du {self.parti} ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'PS_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des revenus et dépenses"""
        ax.plot(df['Annee'], df['Revenus_Total'], label='Revenus Totaux', 
               linewidth=2, color='#FF0000', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Total'], label='Dépenses Totales', 
               linewidth=2, color='#FF6600', alpha=0.8)
        
        ax.set_title('Évolution des Revenus et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Ajouter des annotations pour les événements clés
        key_events = {1971: 'Congrès Epinay', 1981: 'Mitterrand', 1995: 'Chirac', 
                     1997: 'Gauche Plurielle', 2002: 'Défaite Jospin', 
                     2012: 'Hollande', 2017: 'Effondrement'}
        
        for year, event in key_events.items():
            if year in df['Annee'].values:
                y_val = df[df['Annee'] == year]['Revenus_Total'].values[0]
                ax.annotate(event, (year, y_val), xytext=(10, 10), 
                           textcoords='offset points', fontsize=8, 
                           arrowprops=dict(arrowstyle='->', alpha=0.6))
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des revenus"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Cotisations_Adherents', 'Dons_Prives', 'Financement_Public', 
                     'Revenus_Evenements', 'Cotisations_Elus', 'Revenus_Formations']
        colors = ['#FF0000', '#FF6600', '#FF9999', '#CC0000', '#FF3333', '#990000']
        labels = ['Cotisations Adhérents', 'Dons Privés', 'Financement Public', 
                 'Événements', 'Cotisations Élus', 'Formations']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Revenus (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Depenses_Personnel', 'Depenses_Campagnes', 'Depenses_Communication',
                     'Depenses_Fonctionnement', 'Depenses_Formation', 'Depenses_International']
        colors = ['#FF0000', '#FF6600', '#FF9999', '#CC0000', '#FF3333', '#990000']
        labels = ['Personnel', 'Campagnes', 'Communication', 'Fonctionnement', 'Formation', 'International']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_membership_structure(self, df, ax):
        """Plot des adhérents et structure"""
        # Adhérents
        ax.bar(df['Annee'], df['Adherents']/1000, label='Adhérents (milliers)', 
              color='#FF0000', alpha=0.7)
        
        ax.set_title('Adhérents et Structure Territoriale', fontsize=12, fontweight='bold')
        ax.set_ylabel('Adhérents (milliers)', color='#FF0000')
        ax.tick_params(axis='y', labelcolor='#FF0000')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Fédérations en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Federations_Departementales'], label='Fédérations Départementales', 
                linewidth=2, color='#FF6600')
        ax2.set_ylabel('Fédérations Départementales', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_strategic_investments(self, df, ax):
        """Plot des investissements stratégiques"""
        ax.plot(df['Annee'], df['Investissement_Communication'], label='Communication', 
               linewidth=2, color='#FF0000', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Numérique'], label='Numérique', 
               linewidth=2, color='#FF6600', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Formation'], label='Formation', 
               linewidth=2, color='#FF9999', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Recherche'], label='Recherche', 
               linewidth=2, color='#CC0000', alpha=0.8)
        
        ax.set_title('Investissements Stratégiques (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_financial_indicators(self, df, ax):
        """Plot des indicateurs financiers"""
        # Taux d'exécution budgétaire
        ax.bar(df['Annee'], df['Taux_Execution_Budget']*100, label='Taux d\'Exécution (%)', 
              color='#FF0000', alpha=0.7)
        
        ax.set_title('Indicateurs Financiers', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux d\'Exécution (%)', color='#FF0000')
        ax.tick_params(axis='y', labelcolor='#FF0000')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Dépendance financement public en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Dependance_Financement_Public']*100, label='Dépendance Financement Public (%)', 
                linewidth=3, color='#FF6600')
        ax2.set_ylabel('Dépendance Financement Public (%)', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_elected_officials(self, df, ax):
        """Plot de l'évolution des élus"""
        ax.plot(df['Annee'], df['Elus_Locaux']/1000, label='Élus Locaux (milliers)', 
               linewidth=2, color='#FF0000', alpha=0.8)
        
        ax.set_title('Évolution des Élus', fontsize=12, fontweight='bold')
        ax.set_ylabel('Élus Locaux (milliers)', color='#FF0000')
        ax.tick_params(axis='y', labelcolor='#FF0000')
        ax.grid(True, alpha=0.3)
        
        # Élus nationaux en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Elus_Nationaux'], label='Élus Nationaux', 
                linewidth=2, color='#FF6600', alpha=0.8)
        ax2.set_ylabel('Élus Nationaux', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_financial_situation(self, df, ax):
        """Plot de la situation financière"""
        # Solde financier
        ax.bar(df['Annee'], df['Solde_Financier']*100, label='Solde Financier (% du budget)', 
              color=df['Solde_Financier'].apply(lambda x: '#009900' if x > 0 else '#FF0000'), alpha=0.7)
        
        ax.set_title('Situation Financière', fontsize=12, fontweight='bold')
        ax.set_ylabel('Solde Financier (% du budget)', color='#FF0000')
        ax.tick_params(axis='y', labelcolor='#FF0000')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Endettement'], label='Endettement (M€)', 
                linewidth=3, color='#FF6600')
        ax2.set_ylabel('Endettement (M€)', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques pour le PS"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - {self.parti} ({self.start_year}-{self.end_year})")
        print("=" * 70)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Revenus_Total'].mean()
        avg_expenses = df['Depenses_Total'].mean()
        avg_adherents = df['Adherents'].mean()
        avg_execution = df['Taux_Execution_Budget'].mean() * 100
        
        print(f"Revenus moyens annuels: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Adhérents moyens: {avg_adherents:,.0f} personnes")
        print(f"Taux d'exécution budgétaire moyen: {avg_execution:.1f}%")
        
        # 2. Croissance historique
        print("\n2. 📊 ÉVOLUTION HISTORIQUE:")
        revenue_growth = ((df['Revenus_Total'].iloc[-1] / 
                          df['Revenus_Total'].iloc[0]) - 1) * 100
        adherents_growth = ((df['Adherents'].iloc[-1] / 
                           df['Adherents'].iloc[0]) - 1) * 100
        
        print(f"Évolution des revenus ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Évolution des adhérents ({self.start_year}-{self.end_year}): {adherents_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        membership_share = (df['Cotisations_Adherents'].mean() / df['Revenus_Total'].mean()) * 100
        donations_share = (df['Dons_Prives'].mean() / df['Revenus_Total'].mean()) * 100
        public_funding_share = (df['Financement_Public'].mean() / df['Revenus_Total'].mean()) * 100
        elected_share = (df['Cotisations_Elus'].mean() / df['Revenus_Total'].mean()) * 100
        
        print(f"Part des cotisations adhérents: {membership_share:.1f}%")
        print(f"Part des dons privés: {donations_share:.1f}%")
        print(f"Part du financement public: {public_funding_share:.1f}%")
        print(f"Part des cotisations élus: {elected_share:.1f}%")
        
        # 4. Performance et efficacité
        print("\n4. 🎯 PERFORMANCE FINANCIÈRE:")
        avg_balance = df['Solde_Financier'].mean() * 100
        last_debt = df['Endettement'].iloc[-1]
        dependency_public = df['Dependance_Financement_Public'].iloc[-1] * 100
        
        print(f"Solde financier moyen: {avg_balance:.1f}% du budget")
        print(f"Endettement final: {last_debt:.1f} M€")
        print(f"Dépendance au financement public: {dependency_public:.1f}%")
        
        # 5. Spécificités du PS
        print(f"\n5. 🌟 SPÉCIFICITÉS DU PARTI SOCIALISTE:")
        print(f"Orientation politique: {self.config['orientation']}")
        print(f"Électorat cible: {', '.join(self.config['electorat_cible'])}")
        print(f"Sources de financement: {', '.join(self.config['sources_financement'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 1971: Congrès d'Epinay - création du PS moderne")
        print("• 1981: Élection de François Mitterrand")
        print("• 1988: Réélection de Mitterrand")
        print("• 1995: Défaite de Lionel Jospin")
        print("• 1997: Victoire de la gauche plurielle")
        print("• 2002: Défaite historique de Jospin au 1er tour")
        print("• 2007: Défaite de Ségolène Royal")
        print("• 2012: Élection de François Hollande")
        print("• 2017: Effondrement avec Benoît Hamon")
        print("• 2022: Primaires et reconstruction")
        
        # 7. Recommandations stratégiques
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Reconstruire la base militante")
        print("• Diversifier les sources de financement")
        print("• Réduire la dépendance au financement public")
        print("• Moderniser l'appareil du parti")
        print("• Renforcer l'ancrage local et territorial")
        print("• Développer le fundraising numérique")
        print("• Restructurer la dette historique")
        print("• Retrouver une crédibilité économique")

def main():
    """Fonction principale pour l'analyse du PS"""
    print("🏛️ ANALYSE DES FINANCES DU PARTI SOCIALISTE (1971-2025)")
    print("=" * 60)
    
    # Initialiser l'analyseur
    analyzer = PSFinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'PS_financial_data_1971_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Adherents', 'Revenus_Total', 'Depenses_Total', 'Taux_Execution_Budget']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des finances du {analyzer.parti} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Revenus, dépenses, adhérents, élus, indicateurs financiers")

if __name__ == "__main__":
    main()