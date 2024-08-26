from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class UserIDSequence(models.Model):
    current_id = models.IntegerField(default=0)
    def __str__(self):
        return str(self.current_id)
    
class CompanyIDSequence(models.Model):
    current_id = models.IntegerField(default=0)
    def __str__(self):
        return str(self.current_id)
    
class SubUserIDSequence(models.Model):
    current_id = models.IntegerField(default=0)
    def __str__(self):
        return str(self.current_id)

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(null=False)
    phone_number = models.IntegerField(null=False)
    linkedin_url = models.URLField(null=True)
    firstname = models.CharField(max_length=50,null=False)  
    lastname = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=150,null=False)  
    user_type = models.CharField(max_length=12,default='admin')
    company_type = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.user_id:
            user_sequence, created = UserIDSequence.objects.get_or_create(pk=1)
            user_sequence.current_id += 1
            self.user_id = f'NL{user_sequence.current_id:03d}'
            user_sequence.save()
        if self.password:
            # Hash the password
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
    def __str__(self):
        return self.user_id
    
class Company(models.Model):
    # Company Details
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='companies')
    company_id = models.CharField(max_length=10, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True)
    date_of_incorporation = models.DateField(null= True)
    email = models.EmailField(null=True)
    phone=models.IntegerField(null=True)
    website_url = models.URLField(null=True)
    linkedin_url = models.URLField(null=True)   
    business_type = models.CharField(max_length=255, null=True)
    sector = models.CharField(max_length=255, null=True)
    company_type = models.CharField(max_length=10, null=True)
    location = models.CharField(max_length=20, null=True)
    no_of_employees=models.IntegerField(null=True)
    products=models.CharField(max_length=255, null=True)
    competitor=models.CharField(max_length=255, null=True)
    vision=models.CharField(max_length=255, null=True)
    customers=models.IntegerField(null=True)
    current_revenue=models.DecimalField(decimal_places=2, max_digits=25, null=True)
    current_pl=models.DecimalField(decimal_places=2, max_digits=25, null=True)
    previous_revenue=models.DecimalField(decimal_places=2, max_digits=25, null=True)
    previous_pl=models.DecimalField(decimal_places=2, max_digits=25, null=True)
    a_yearbefore_revenue=models.DecimalField(decimal_places=2, max_digits=25, null=True)
    a_yearbefore_pl=models.DecimalField(decimal_places=2, max_digits=25, null=True)
    additional=models.TextField(null=True)


    def save(self, *args, **kwargs):
        if not self.company_id:
            company_sequence, created = CompanyIDSequence.objects.get_or_create(pk=1)
            company_sequence.current_id += 1
            self.company_id = f'C{company_sequence.current_id:03d}'
            company_sequence.save()
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.company_id

class CompanyProfile(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='company_profiles')
    tam = models.FloatField()
    cagr = models.FloatField()
    number_of_clients_users = models.IntegerField()
    previous_year_revenue = models.FloatField()
    current_year_revenue_arr = models.FloatField()
    current_monthly_burn_rate = models.FloatField()
    forecasted_revenue_for_next_year = models.FloatField()
    business_stage = models.ForeignKey('BusinessStage', on_delete=models.CASCADE)
    equity_funds_raised_so_far = models.FloatField()
    funds_needed = models.FloatField()
    business_plan = models.FileField(upload_to='business_plan',null=True)
    pitch_video = models.FileField(upload_to='pitch',null=True)
    product_video = models.FileField(upload_to='product',null=True)

class CompanyAsk(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    ask=models.IntegerField(null=True)
    valuation=models.IntegerField(null=True)
    equity_share=models.DecimalField(decimal_places=1, null=True, max_digits=5)
    details=models.TextField()
    

class Sector(models.Model):
    #company_id=models.ForeignKey(Company, on_delete=models.CASCADE,related_name='sectors')
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class BusinessType(models.Model):
    #company_id=models.ForeignKey(Company, on_delete=models.CASCADE,related_name='business_types')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BusinessStage(models.Model):
    #company_id=models.ForeignKey(Company, on_delete=models.CASCADE,related_name='business_stages')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Founder(models.Model):
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE,related_name='founders')
    name=models.CharField(max_length=50)
    linkedin_url=models.URLField()
    short_profile=models.TextField(null=True)
    photo=models.ImageField(upload_to='founder_photos',null=True)
    title=models.CharField(null=True, max_length=20)
    date_joined=models.DateField(null=True)
    def __str__(self):
        return self.name

class ExecutiveMember(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='executive_members')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Advisor(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='advisors')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='challenges')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SolvedProblem(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='solved_problems')
    description = models.TextField()

    def __str__(self):
        return self.description

class Competitor(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='competitors')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class SocialMedia(models.Model):
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='social_media_urls')
    #name=models.CharField(max_length=25)
    url=models.URLField()

class Client(models.Model):
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE,related_name='clients')
    name=models.CharField(max_length=25)
    logo=models.ImageField(upload_to='clients_logo',null=True)

class CapTable(models.Model):
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE,related_name='cap_tables')
    name = models.CharField(max_length=200)
    shareholder=models.CharField(max_length=50, null=True)
    percentage_of_shares= models.DecimalField(max_digits=5,decimal_places=2)
    investedsince=models.DateField(null=True)
    amount=models.IntegerField(null=True)
    valuation=models.IntegerField(null=True)
    details=models.TextField(null=True)




class Team(models.Model):
    subuser_id = models.CharField(max_length=10, primary_key=True)
    #creator_id = models.ForeignKey(User,on_delete=models.CASCADE)
    creator_id = models.CharField(max_length=15)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(null=False)
    phone_number = models.IntegerField(null=False)
    linkedin_url = models.URLField(null=True)
    firstname = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=10,null=False)  
    user_type = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        if not self.subuser_id:
            subuser_sequence, created = SubUserIDSequence.objects.get_or_create(pk=1)
            subuser_sequence.current_id += 1
            self.subuser_id = f'SUBNL{subuser_sequence.current_id:03d}'
            subuser_sequence.save()
        if self.password:
            # Hash the password
            self.password = make_password(self.password)
        super(Team, self).save(*args, **kwargs)
    def __str__(self):
        return self.subuser_id

class productsandservices(models.Model):
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    launch_date=models.DateField()
    description=models.TextField()
    industry=models.CharField(max_length=100)
    type_of_business=models.CharField(max_length=100)
    problem_solved=models.TextField()
    current_year_revenue=models.IntegerField()
    previous_year_revenue=models.IntegerField()
    a_year_before_revenue=models.IntegerField()
    current_year_pl=models.IntegerField()
    previous_year_pl=models.IntegerField()
    a_year_before_pl=models.IntegerField()
    customers=models.TextField()
    competitors=models.TextField()



class IncomeStatement(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    date = models.DateTimeField()

    total_revenue = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    operating_revenue = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cost_of_revenue = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gross_profit = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    operating_expense = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    selling_general_and_administrative_expense = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    general_and_administrative_expenses = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    selling_and_marketing_expense = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    research_and_development_expense = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    operating_income = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    net_non_operating_interest_income_expense= models.DecimalField(max_digits=10, decimal_places=2,null=True)
    interest_income_non_operating = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    interest_expense_non_operating = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_income_or_expense = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gain_or_loss_on_sale_of_security = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    special_income_or_charges = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    write_off = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_non_operating_income_or_expenses = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    pretax_income = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    tax_provision = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    net_income = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    preference_share_dividends = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    net_income_to_common_stockholders = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    equity_share_dividends = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    retained_earnings = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    basic_eps = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    diluted_eps = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    depreciation_and_amortization = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    ebitda = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    no_of_equity_shares = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    
    monthly_or_quarterly_or_yearly = models.CharField(max_length=15,null=True)

    creator_id = models.CharField(max_length=12,null=True)
    modifier_id = models.CharField(max_length=12,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)


class BalanceSheet(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    date = models.DateTimeField()

    
    total_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    current_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cash_cash_equivalents_and_short_term_investments = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cash_and_cash_equivalents = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cash_equivalents = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_short_term_investments = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    receivables = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    accounts_receivable = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gross_accounts_receivable = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    allowance_for_doubtful_accounts_receivable = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_receivables = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    inventory = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    raw_materials = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    work_in_process = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    finished_goods = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    hedging_current_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_current_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    total_non_current_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    net_ppe = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    gross_ppe = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    land_and_improvements = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    buildings_and_improvements = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    machinery_furniture_equipment = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_properties = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    leases = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    accumulated_depreciation = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    goodwill_and_other_intangible_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    goodwill = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_intangible_assets = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    investments_and_advances = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    long_term_equity_investment = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    other_non_current_assets = models.CharField(max_length=12,null=True)
    total_liabilities_net_minority_interest = models.CharField(max_length=12,null=True)
    current_liabilities = models.CharField(max_length=12,null=True)
    payables_and_accrued_expenses = models.CharField(max_length=12,null=True)
    accounts_payable = models.CharField(max_length=12,null=True)
    income_tax_payable = models.CharField(max_length=12,null=True)
    pension_and_other_post_retirement_benefit_plans_current = models.CharField(max_length=12,null=True)
    current_debt_and_capital_lease_obligation = models.CharField(max_length=12,null=True)
    current_debt = models.CharField(max_length=12,null=True)
    capital_lease_obligation = models.CharField(max_length=12,null=True)
    current_deferred_liabilities = models.CharField(max_length=12,null=True)
    current_deferred_revenue = models.CharField(max_length=12,null=True)
    other_current_liabilities = models.CharField(max_length=12,null=True)
    total_non_current_liabilities_net_minority_interest = models.CharField(max_length=12,null=True)
    long_term_debt_and_capital_lease_obligation = models.CharField(max_length=12,null=True)
    long_term_debt = models.CharField(max_length=12,null=True)
    long_term_capital_lease_obligation = models.CharField(max_length=12,null=True)
    non_current_deferred_liabilities = models.CharField(max_length=12,null=True)
    non_current_deferred_taxes_liabilities = models.CharField(max_length=12,null=True)
    non_current_deferred_revenue = models.CharField(max_length=12,null=True)
    trade_and_other_payables_non_current = models.CharField(max_length=12,null=True)
    other_non_current_liabilities = models.CharField(max_length=12,null=True)
    total_equity_gross_minority_interest = models.CharField(max_length=12,null=True) 
    stockholders_equity = models.CharField(max_length=12,null=True)
    capital_stock = models.CharField(max_length=12,null=True)
    common_stock = models.CharField(max_length=12,null=True)
    retained_earnings = models.CharField(max_length=12,null=True)
    gains_or_losses_not_affecting_retained_earnings = models.CharField(max_length=12,null=True)
    other_equity_adjustments = models.CharField(max_length=12,null=True)

    monthly_or_quarterly_or_yearly = models.CharField(max_length=15,null=True)

    creator_id = models.CharField(max_length=12,null=True)
    modifier_id = models.CharField(max_length=12,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)



class CashFlow(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    date = models.DateTimeField()
    operating_cash_flow = models.CharField(max_length=12,null=True)
    net_income_from_continuing_operations = models.CharField(max_length=12,null=True)
    depreciation_and_amortization = models.CharField(max_length=12,null=True)
    change_in_working_capital = models.CharField(max_length=12,null=True)
    changes_in_receivables = models.CharField(max_length=12,null=True)
    change_in_inventory = models.CharField(max_length=12,null=True)
    change_in_hedging_assets_current = models.CharField(max_length=12,null=True)
    change_in_other_current_assets = models.CharField(max_length=12,null=True)
    change_in_payables_and_accrued_expense = models.CharField(max_length=12,null=True)
    change_in_pension_and_other_post_retirement_benefit_plans_current = models.CharField(max_length=12,null=True)
    change_in_current_debt_and_capital_lease_obligation = models.CharField(max_length=12,null=True)
    change_in_current_deferred_liabilities = models.CharField(max_length=12,null=True)
    change_in_other_current_liabilities = models.CharField(max_length=12,null=True)
    investing_cash_flow = models.CharField(max_length=12,null=True)
    cash_flow_from_continuing_investing_activities = models.CharField(max_length=12,null=True)
    net_ppe_purchase_and_sale = models.CharField(max_length=12,null=True)
    goodwill_and_other_intangible_assets = models.CharField(max_length=12,null=True)
    investments_and_advances = models.CharField(max_length=12,null=True)
    other_non_current_assets = models.CharField(max_length=12,null=True)
    financing_cash_flow = models.CharField(max_length=12,null=True)
    cash_flow_from_continuing_financing_activities = models.CharField(max_length=12,null=True)
    long_term_debt_and_capital_lease_obligation = models.CharField(max_length=12,null=True)
    non_current_deferred_liabilities = models.CharField(max_length=12,null=True)
    trade_and_other_payables_non_current = models.CharField(max_length=12,null=True)
    other_non_current_liabilities = models.CharField(max_length=12,null=True)
    common_stock_issuance_payments = models.CharField(max_length=12,null=True)
    common_stock_dividend_paid = models.CharField(max_length=12,null=True)
    end_cash_position = models.CharField(max_length=12,null=True)
    changes_in_cash = models.CharField(max_length=12,null=True)
    beginning_cash_position = models.CharField(max_length=12,null=True)
    capital_expenditure = models.CharField(max_length=12,null=True)
    issuance_repurchase_of_capital_stock = models.CharField(max_length=12,null=True)
    repayment_of_debt = models.CharField(max_length=12,null=True)
    free_cash_flow = models.CharField(max_length=12,null=True)

    monthly_or_quarterly_or_yearly = models.CharField(max_length=15,null=True)

    creator_id = models.CharField(max_length=12,null=True)
    modifier_id = models.CharField(max_length=12,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)




    




