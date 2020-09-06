from pygame import mixer 
import time
ltime=time.asctime( time.localtime(time.time()))
def health():

    ticks =list(time.asctime( time.localtime(time.time())))
    localtime=ticks[11:16]
    hour=int(localtime[0])*10+int(localtime[1])
    minutes=int(localtime[3])*10+int(localtime[4])
    timemin=hour*60+minutes

    while timemin>100 and timemin<=400:
        ticks =list(time.asctime( time.localtime(time.time())))
        localtime=ticks[11:16]
        hour=int(localtime[0])*10+int(localtime[1])
        minutes=int(localtime[3])*10+int(localtime[4])
        timemin=hour*60+minutes

        if timemin%30== 0 and timemin%90 != 0 and timemin%150 != 0:
            eyelog()
            time.sleep(60)

        if timemin%90 == 0 and timemin%30 != 0 and timemin%150 != 0:
            waterlog()
            time.sleep(60)

        if timemin%30 != 0 and timemin%90 != 0 and timemin%150 == 0:
            exerciselog()
            time.sleep(60)

        if timemin%30 == 0 and timemin%90 == 0 and timemin%150 != 0:
            eyelog()
            time.sleep(10)
            waterlog()
            time.sleep(50)

        if timemin%30 == 0 and timemin%90 != 0 and timemin%150 == 0:
            eyelog()
            time.sleep(10)
            exerciselog()
            time.sleep(50)

        if timemin%30 != 0 and timemin%90 == 0 and timemin%150 == 0:
            waterlog()
            time.sleep(10)
            exerciselog()
            time.sleep(50)

        if timemin%30 == 0 and timemin%90 == 0 and timemin%150 == 0:
            eyelog()
            time.sleep(10)
            waterlog()
            time.sleep(10)
            exerciselog()
            time.sleep(40)



def eyelog():
    done=eye()
    if(done==1):
        f=open("eye.txt","a")
        f.write(ltime+"eye exercise done\n")
        f.close()

def waterlog():
    done=water()
    counter=1     #should be less than 18 as the person will drink 200 ml and his daily dose is 3.5 l
    if(done==1 and counter<19):
        f=open("water.txt","a")
        f.write(ltime+" water has been drank\n ")
        f.close()
        counter=counter+1


def exerciselog():
    done=exercise()
    if(done==1):
        f=open("exercise.txt","a")
        f.write(ltime +"exercise done\n")
        f.close()

# Starting the mixer 
def eye():
    mixer.init() 

    # Loading the song 
    mixer.music.load("eye.mp3") 

    # Setting the volume 
    mixer.music.set_volume(0.7) 

    # Start playing the song 
    mixer.music.play() 
    done=0
    # infinite loop 
    while True: 
        
        print("Press 'eyedone' to stop the song") 
        query = input(" ") 
        
        if query == 'eyedone': 
            # Stop the mixer 
            mixer.music.stop() 
            done=1
            break
    return done
def exercise():
    mixer.init() 
    done=0
    # Loading the song 
    mixer.music.load("exercise.mp3") 

    # Setting the volume 
    mixer.music.set_volume(0.3) 

    # Start playing the song 
    mixer.music.play() 

    # infinite loop 
    while True: 
        
        print("Press exercisedone to stop the song") 
        query = input(" ") 
        
        if query == 'exercisedone': 
            # Stop the mixer 
            mixer.music.stop()
            done=1 
            break
    return done
def water():
    mixer.init() 
    done=0
    # Loading the song 
    mixer.music.load("water.mp3") 

    # Setting the volume 
    mixer.music.set_volume(0.3) 

    # Start playing the song 
    mixer.music.play() 

    # infinite loop 
    while True: 
        
        print("Press waterdone to stop the song") 
        query = input(" ") 
        
        if query == 'waterdone': 
            # Stop the mixer 
            mixer.music.stop() 
            done=1
            break
    return done

if __name__ == "__main__":
        health()
