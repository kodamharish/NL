from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL 
    path('',home,name='home'), # Home URL
    path('home',home,name='home'),
    path('about',about,name='about'),
    path('services',services,name='services'),
    path('contact',contact,name='contact'),


    #login,logout
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    #path('sign_up',signup,name='sign_up'),
    path('signup',signup,name='signup'),

    #path('investor_sign_up',investorSignUp,name='investor_sign_up'),
    #path('ca_firm_sign_up',caFirmSignUp,name='ca_firm_sign_up'),

    #Super Admin
    path('super_admin_dashboard',superAdminDashboard,name='super_admin_dashboard'),
    path('admins',admins,name='admins'),
    path('editors',editors,name='editors'),
    path('users',users,name='users'),
    path('startups',startups,name='startups'),
    path('investors',investors,name='investors'),
    path('ca_firms',ca_firms,name='ca_firms'),
    path('companies',companies,name='companies'),


    #Admin
    #path('admin_dashboard/<str:id>/',adminDashboard,name='admin_dashboard'),
    path('admin_dashboard',adminDashboard,name='admin_dashboard'),

    
    #company
    path('add_company',addCompany,name='add_company'), 
    path('company_profile/<str:id>/',companyProfile,name='company_profile'),
    path('founders/<str:id>/', founders, name='founders'),

    path('basic_information/<str:id>/',basicInformation,name='basic_information'),
    path('business_plan/<str:id>/',businessPlan,name='business_plan'),
    path('pitch_and_product/<str:id>/',pitchAndProduct,name='pitch_and_product'),
    

    path('cap_table/<str:id>/',capTable,name='cap_table'),
    path('company_ask/<str:id>/', company_ask, name='company_ask'),



    path('income_statement/<str:id>/',incomeStatement,name='income_statement'), 
    path('balance_sheet/<str:id>/',balanceSheet,name='balance_sheet'), 
    path('cash_flow/<str:id>/',cashFlow,name='cash_flow'),
    

    
    #investor 
    path('investor_dashboard',investorDashboard,name='investor_dashboard'),
    path('investor_base/<str:id>/',investorBase,name='investor_base'),
    path('founders_and_team/<str:id>/',founderAndTeam,name='founders_and_team'),
   #Planning & Budgeting
    path('planning_budgeting_income_statement_table/<str:id>/',incomeStatementTable,name='planning_budgeting_income_statement_table'), 
    path('planning_budgeting_balance_sheet_table/<str:id>/',balanceSheetTable,name='planning_budgeting_balance_sheet_table'), 
    path('planning_budgeting_cash_flow_table/<str:id>/',cashFlowTable,name='planning_budgeting_cash_flow_table'),
    path('cash_flow_manual_entry/<str:id>/', cashflowmanualentry, name='cash_flow_manual_entry'),
    path('cashflowfirstyear/<str:id>/', cashflowfirstyearofoperations, name='cashflowfirstyearofoperations'),

    #Forecasting
    path('forecasting_income_statement_table/<str:id>/',forecastedIncomeStatementTable,name='forecasting_income_statement_table'),
    path('forecasting_balance_sheet_table/<str:id>/',forecastedBalanceSheetTable,name='forecasting_balance_sheet_table'),
    path('forecasting_cash_flow_table/<str:id>/',forecastedCashFlowTable,name='forecasting_cash_flow_table'),    

    path('forecasting_income_statement_table/<str:id>/',incomeStatementTable,name='forecasting_income_statement_table'),
    #path('forecasting_balance_sheet_table/<str:id>/',balanceSheetTable,name='forecasting_balance_sheet_table'), 
    #path('forecasting_cash_flow_table/<str:id>/',cashFlowTable,name='forecasting_cash_flow_table'), 

    # path('financial_statement/<str:id>/',financialStatement,name='financial_statement'),
    # path('revenue_verticals/<str:company_id>/',revenueVerticals,name='revenue_verticals'),
    # path('expenses/<str:company_id>/',expenses,name='expenses'),

    #children
    path('my_team',myTeam,name='my_team'),
    path('add_team',addTeam,name='add_team'),
    path('update_team/<str:id>',updateTeam,name='update_team'),
    path('delete_team/<str:id>',deleteTeam,name='delete_team'),

    path('parent',parent,name='parent'),
    #path('profit_loss_balance_sheet',profitLossBalanceSheetCalculation,name='profit_loss_balance_sheet'),

    #editor
    path('editor_dashboard',editorDashboard,name='editor_dashboard'),
    #user
    path('user_dashboard',userDashboard,name='user_dashboard'),

    #password reset
    path('forgot_password_1',forgotPasswordOne,name='forgot_password_1'),
    path('forgot_password_2',forgotPasswordTwo,name='forgot_password_2'),

]