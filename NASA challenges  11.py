#Name: Rishi Doreswamy
#Graphs from previous NASA questions
#NASA Centienel challenges 
#July 2021   
#import panda
#import mathlibs 
def main():
    from pandas import DataFrame, read_csv
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    import pandas as pd 
    pp = PdfPages('Centennial Challenge Survey.pdf')
    #open file to succesfully read 
    file = r'C:\Users\rish4\OneDrive\Documents\data.xlsx'
    df = pd.read_excel(file)
    print("file succesfully open")
    #file succesfully open 
    print(file)
    
    #NASA assoication 
    
    # ignore 'N/A' when poltting
    df = df[df['NASA Association'] != 'N/A']
    fig=plt.figure(0)
    df['NASA Association'].plot(kind="hist")
    plt.xlabel("Ranking")
    #print ranking for x label  
    plt.title("Reason for participation:NASA assoication")
    #print title 
    plt.show
    pp.savefig(fig)
    df = df[df['Interesting Work'] != 'N/A']
    fig=plt.figure(1)
    #plot figure 1 
    
    #Intresting work 
    df['Interesting Work'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title("Reason for particpation:Intresting work")
    plt.show
    pp.savefig(fig)
 
    #Feedback 

    df=df[df['Feedback'] !='N/A']
    fig=plt.figure(2)
    df['Feedback'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title("Reason for particpation: Feedback")
    plt.show
    pp.savefig(fig)
    
    #Mentoring 
    df=df[df['Mentoring '] !='N/A']
    fig=plt.figure(3)
    df['Mentoring '].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title("Reason for particpation: Mentoring")
    plt.show
    pp.savefig(fig)
    
    #next plot: Media or brand exposure 
    df=df[df['Media or brand exposure'] !='N/A']
    fig=plt.figure(4)
    df['Media or brand exposure'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title("Reason for particpation:Media or brand exposure")
    plt.show
    pp.savefig(fig)
    
    #networking oppturnties 
    df=df[df["Networking opportunities "] !='N/A']
    fig=plt.figure(5)
    df['Networking opportunities '].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title('Reason for particpation:Networking opportunities')
    plt.show
    pp.savefig(fig)
    
    #collabration opportunities 
    df=df[df["Collaboration opportunities"]!='N/A']
    fig=plt.figure(6)
    df['Collaboration opportunities'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title('Reason for participating:Collaboration opportunities')
    plt.show
    pp.savefig(fig)
    
    #prize purse 
    df=df[df["Prize Purse"] !='N/A']
    fig=plt.figure(7)
    df['Prize Purse'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title('Reason for particpation:Prize Purse')
    plt.show
    pp.savefig(fig)
    
    #testing of your solution 
    df=df[df["Testing of your solution"] !='N/A']
    fig=plt.figure(8)
    df['Testing of your solution'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title('Reason for particpation: Testing of your solution')
    plt.show
    pp.savefig(fig)
    
    #Applying existing technolgy 
    df=df[df["Applying existing technology in a new way"] !='N/A']
    fig=plt.figure(9)
    df['Applying existing technology in a new way'].plot(kind="hist")
    plt.xlabel("Ranking")
    plt.title('Reason for particpation:Applying existing technology in a new way')
    plt.show
    pp.savefig(fig)
    pp.close()
main()
#pp.close

    
   
