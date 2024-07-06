import os
import shutil
 
def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)

print("Juegos en la carpeta DOSGames")
print("1- Grand Prix 2")
print("2- Nascar Racing")
print("3- Nascar Racing 2")
print("4- Indianapolis 500")
print("5- Indycar Racing")
print("6- Indicar Racing 2")
print("7- Carlos Sainz Rally")
print("Que juego quieres lanzar:")
option = input()
print(f"Has elegido: {option}, lanzando DOSBox")
if option == "1":   
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "GP2.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)           
if option == "2":    
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "Nascar.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)           
if option == "3":    
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "Nascar2.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)  
if option == "4":    
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "Indy500.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)  
if option == "5":    
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "Indy1.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)
if option == "6":    
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "Indy2.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)
if option == "7":    
    # Source and destination file paths
    source_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "Carlos.conf")
    destination_file = os.path.join("C:/Users/berto/AppData/Local/DOSBox", "dosbox-0.74.conf")
    # Copy and replace    
    copy_and_replace(source_file, destination_file)    

os.system("F:\DOSBox-0.74\DOSBox.exe")