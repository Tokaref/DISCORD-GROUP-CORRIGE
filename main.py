import pyautogui
import itertools
import colorama
import time
import os
import pystyle
from pystyle import Colors
from time import sleep


os.system("title GROUPE ")

colorama.init(autoreset=True)

class pao:
    def __init__(self):
        pystyle.Write.Print('''                        

     *******   **  ********   ******    *******   *******   *******  
    /**////** /** **//////   **////**  **/////** /**////** /**////** 
    /**    /**/**/**        **    //  **     //**/**   /** /**    /**
    /**    /**/**/*********/**       /**      /**/*******  /**    /**
    /**    /**/**////////**/**       /**      /**/**///**  /**    /**
    /**    ** /**       /**//**    **//**     ** /**  //** /**    ** 
    /*******  /** ********  //******  //*******  /**   //**/*******  
    ///////   // ////////    //////    ///////   //     // ///////  

''', Colors.green_to_red, interval=0)
        sleep(0.3)
        os.system("cls")

        
pao()
class po:
    def __init__(self):
        pystyle.Write.Print('''                        

     *******   **  ********   ******    *******   *******   *******  
    /**////** /** **//////   **////**  **/////** /**////** /**////** 
    /**    /**/**/**        **    //  **     //**/**   /** /**    /**
    /**    /**/**/*********/**       /**      /**/*******  /**    /**
    /**    /**/**////////**/**       /**      /**/**///**  /**    /**
    /**    ** /**       /**//**    **//**     ** /**  //** /**    ** 
    /*******  /** ********  //******  //*******  /**   //**/*******  
    ///////   // ////////    //////    ///////   //     // ///////  

''', Colors.cyan_to_green, interval=0)
        sleep(0.3)
        os.system("cls")


po()
class pa1o:
    def __init__(self):
        pystyle.Write.Print('''                        

     *******   **  ********   ******    *******   *******   *******  
    /**////** /** **//////   **////**  **/////** /**////** /**////** 
    /**    /**/**/**        **    //  **     //**/**   /** /**    /**
    /**    /**/**/*********/**       /**      /**/*******  /**    /**
    /**    /**/**////////**/**       /**      /**/**///**  /**    /**
    /**    ** /**       /**//**    **//**     ** /**  //** /**    ** 
    /*******  /** ********  //******  //*******  /**   //**/*******  
    ///////   // ////////    //////    ///////   //     // ///////  

''', Colors.blue_to_white, interval=0)
        sleep(0.3)
        os.system("cls")

pa1o()
class po2:
    def __init__(self):
        pystyle.Write.Print('''                        

     *******   **  ********   ******    *******   *******   *******  
    /**////** /** **//////   **////**  **/////** /**////** /**////** 
    /**    /**/**/**        **    //  **     //**/**   /** /**    /**
    /**    /**/**/*********/**       /**      /**/*******  /**    /**
    /**    /**/**////////**/**       /**      /**/**///**  /**    /**
    /**    ** /**       /**//**    **//**     ** /**  //** /**    ** 
    /*******  /** ********  //******  //*******  /**   //**/*******  
    ///////   // ////////    //////    ///////   //     // ///////  

''', Colors.blue_to_purple, interval=0)
        sleep(0.3)
        os.system('cls')
        

po2()    

class p1o2:
    def __init__(self):
        pystyle.Write.Print('''                        

     *******   **  ********   ******    *******   *******   *******  
    /**////** /** **//////   **////**  **/////** /**////** /**////** 
    /**    /**/**/**        **    //  **     //**/**   /** /**    /**
    /**    /**/**/*********/**       /**      /**/*******  /**    /**
    /**    /**/**////////**/**       /**      /**/**///**  /**    /**
    /**    ** /**       /**//**    **//**     ** /**  //** /**    ** 
    /*******  /** ********  //******  //*******  /**   //**/*******  
    ///////   // ////////    //////    ///////   //     // ///////  

''', Colors.blue_to_cyan, interval=0)
        sleep(0.3)
        

p1o2()      

class interface:
    def __init__(self):   
        print("   ")
        pystyle.Write.Print("   [ ] *GROUPE* (1)", Colors.blue_to_green, interval=0.03)
        print("        ")


interface()        

while True:
    x=int(input())
    if x==1:
        print("        ")
        pystyle.Write.Print("   [ ] VOUS AVEZ CHOISI LE MODE GROUPE !", Colors.blue_to_green, interval=0.03)
        print("        ")
        pystyle.Write.Print("   [ ] *indiquez le nombre d'éxécution *", Colors.blue_to_green, interval=0)
        mot = input()
        print("        ")
        pystyle.Write.Print("   [ ] MODE GROUPE ! ",Colors.blue_to_green, interval=0.03)
        print("        ")
        pystyle.Write.Print("   [ ] *Lancer le programme en appuyant sur 2 *", Colors.blue_to_green, interval=0)
            
    if x==2:
        os.system("cls")
        p1o2()      
        interface()

        num = int(mot)
        for _ in itertools.repeat((mot), num):
            
            pyautogui.click(x=1862, y=80)
            pyautogui.click(x=1857, y=140)
            pyautogui.click(x=1862, y=80)
            pyautogui.click(x=1838, y=209)
            pyautogui.click(x=1862, y=80)









    



