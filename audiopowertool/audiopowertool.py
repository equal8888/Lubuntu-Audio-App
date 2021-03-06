#!/usr/bin/python3
from tkinter import *  					# the GUI toolkit.
from tkinter import ttk					# Define Pages and Separators
import tkinter.messagebox   			# Messagebox About page
import subprocess						# for pulseaudio config

top = Tk()
def main():

# ---------- Define MainFrame ----------

    mainFrame=Frame(top,relief="sunken",border=1)
    Description=Label(mainFrame,text="Audio Powertool:")

    mainFrame.master.title("Audio Powertool for Lubuntu 16.04.3 LTS")
    mainFrame.master.resizable(False, False)

# End ----------

# ---------- Define Pages ----------

	# Menu for pages
    nb=ttk.Notebook(mainFrame.master)
    nb.grid(row=1,column=1,sticky='NESW')

	# Page 1 PulseAudio
    page1=ttk.Frame(nb)
    nb.add(page1,text='PulseAudio (Software Mixer)')

	# Page 2 ALSA
    page2=ttk.Frame(nb)
    nb.add(page2,text='ALSA (Hardware Mixer)')

	# Page 3 Config
    page3=ttk.Frame(nb)
# Page 3 is hidden because features might not work
#    nb.add(page3,text='System Config (OS)')

# End ----------

# -------------------- Tab 1 (PulseAudio) --------------------
    # page1 main frame
    frame0=LabelFrame(page1,bd=5,bg="blue3")
    frame0.grid(row=0,column=0,sticky='NESW')

    # page1 frame
    frame1=LabelFrame(frame0,bd=5,bg="black")
    frame1.grid(row=0,column=1,rowspan=5,sticky='NESW')

	# PulseAudio Status and output info frame (white)
    frame2=Label(frame1)
    frame2.grid(row=2,column=3,columnspan=2,rowspan=2,sticky='es',padx=6)

# ---------- Show Info ----------

# show current PA status from button
    label=Label(frame2,textvariable=vPaRun,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(sticky='NESW')

# show current PA output from button
    label=Label(frame2,textvariable=ShvPaOut,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(sticky='NESW')

# Bitdepth Samplerate
    label=Label(frame1,textvariable=vPaBitdepth,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=0,column=1,sticky='nsw')

# Primary Samplerate
    label=Label(frame1,textvariable=vPaPriRate,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=1,columnspan=4,sticky='nsw')

# Alternative Samplerate
    label=Label(frame1,textvariable=vPaAltRate,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=2,column=1,columnspan=4,sticky='nsw')

# Resampling
    label=Label(frame1,textvariable=vPaRe,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=3,column=1,columnspan=4,sticky='nsw')

# Shortcut to get what I want atm.... (gui fix)
    label=Label(frame1,bg="black",text="--------------------------",font=('Monospace Regular',11))
    label.grid(row=0,column=2,sticky='nsw')

# End ----------

	# Label Resample method rowspan=4
    label=Label(frame0,text=" 1) Bit Depth ",font=('Monospace Regular',11))
    label.grid(row=0,column=0,sticky='NESW')

# ---------- BithDepth Radio Buttons ----------

	# Set the BithDepth value to Default for variable vPaBitdepth
    RadBit16=Radiobutton(frame0,text='Default',font=('Monospace Regular',11),variable=vPaBitdepth,value='; default-sample-format = s16le',command=Pabitdepth,width=8)
    RadBit16.grid(row=1,column=0,sticky='nsw')

	# Set the BithDepth value to 16 Bit for variable vPaBitdepth
    RadBit16=Radiobutton(frame0,text='16 Bit',font=('Monospace Regular',11),variable=vPaBitdepth,value='  default-sample-format = s16le',command=Pabitdepth,width=8)
    RadBit16.grid(row=2,column=0,sticky='nsw')

    # Set the BithDepth value to 24 Bit for variable vPaBitdepth
    RadBit24=Radiobutton(frame0,text='24 Bit',font=('Monospace Regular',11),variable=vPaBitdepth,value='  default-sample-format = s24le',command=Pabitdepth,width=8)
    RadBit24.grid(row=3,column=0,sticky='nsw')

    # Set the BithDepth value to 32 Bit for variable vPaBitdepth
    RadBit32=Radiobutton(frame0,text='32 Bit',font=('Monospace Regular',11),variable=vPaBitdepth,value='  default-sample-format = s32le',command=Pabitdepth,width=8)
    RadBit32.grid(row=4,column=0,sticky='nsw')

# End ----------

# ---------- Primary Samplerate Radio Buttons ----------

	# samplerate frame
    frame4=LabelFrame(page1)
    frame4.grid(row=5,column=0,columnspan=2,sticky='NESW')

	# Label
    label=Label(frame4,text=" 2) Primary Sample Rate         ",font=('Monospace Regular',11))
    label.grid(row=1,column=1,sticky='w')

	# Set the BithDepth value to default for variable vPaBitdepth
    RadPriRateDefault=Radiobutton(frame4,text='Default',font=('Monospace Regular',11),variable=vPaPriRate,value='; default-sample-rate = 44100',command=PaPriRate,width=10)
    RadPriRateDefault.grid(row=1,column=2,sticky='NESW')

	# Set the BithDepth value to 44,100 Hz for variable vPaBitdepth
    RadPriRate44100=Radiobutton(frame4,text='44,100 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='  default-sample-rate = 44100',command=PaPriRate,width=10)
    RadPriRate44100.grid(row=1,column=3,sticky='NESW')

	# Set the BithDepth value to 48,000 Hz for variable vPaBitdepth
    RadPriRate48000=Radiobutton(frame4,text='48,000 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='  default-sample-rate = 48000',command=PaPriRate,width=10)
    RadPriRate48000.grid(row=1,column=4,sticky='NESW')

	# Set the BithDepth value to 88,200 Hz for variable vPaBitdepth
    RadPriRate88200=Radiobutton(frame4,text='88,200 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='  default-sample-rate = 88200',command=PaPriRate,width=10)
    RadPriRate88200.grid(row=1,column=5,sticky='NESW')

	# Set the BithDepth value to 96,000 Hz for variable vPaBitdepth
    RadPriRate96000=Radiobutton(frame4,text='96,000 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='  default-sample-rate = 96000',command=PaPriRate,width=10)
    RadPriRate96000.grid(row=1,column=6,sticky='NESW')

# End ----------

# ---------- Alternative Samplerate Radio Buttons ----------

	# Label
    label=Label(frame4,text=" 3) Alternative Sample Rate ",font=('Monospace Regular',11))
    label.grid(row=2,column=1,sticky='w')

	# Set the BithDepth value to default for variable vPaAltRate
    RadAltRateDefault=Radiobutton(frame4,text='Default',font=('Monospace Regular',11),variable=vPaAltRate,value='; alternate-sample-rate = 48000',command=PaAltRate,width=10)
    RadAltRateDefault.grid(row=2,column=2)

	# Set the BithDepth value to 48,000 Hz for variable vPaAltRate
    RadAltRate48000=Radiobutton(frame4,text='44,100 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='  alternate-sample-rate = 44100',command=PaAltRate,width=10)
    RadAltRate48000.grid(row=2,column=3)

	# Set the BithDepth value to 88,200 Hz for variable vPaAltRate
    RadAltRate48000=Radiobutton(frame4,text='48,000 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='  alternate-sample-rate = 48000',command=PaAltRate,width=10)
    RadAltRate48000.grid(row=2,column=4)

	# Set the BithDepth value to 96,000 Hz for variable vPaAltRate
    RadAltRate96000=Radiobutton(frame4,text='88,200 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='  alternate-sample-rate = 88200',command=PaAltRate,width=10)
    RadAltRate96000.grid(row=2,column=5)

	# Set the BithDepth value to 192,000 Hz for variable vPaAltRate
    RadAltRate192000=Radiobutton(frame4,text='96,000 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='  alternate-sample-rate = 96000',command=PaAltRate,width=10)
    RadAltRate192000.grid(row=2,column=6)

# End ----------

# ---------- Resample method Radio Buttons ----------

    frame5=Frame(page1)
    frame5.grid(row=9,column=0,sticky='NESW')

	# frame for resample method txt
    frame4=Label(frame5)
    frame4.grid(row=1,column=1,sticky='NESW')

    # Label Resample method
    label=Label(frame4,text=" 4) Resample method                  ",font=('Monospace Regular',11))
    label.grid(row=1,column=1,columnspan=2,sticky='NESW')

	# Set the Resample value to speexfloat-10 for variable vPaRe
    vPaRespeexfloat10=Radiobutton(frame5,indicatoron=0,text='speexfloat-10',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = speex-float-10',command=PaRe,width=16)
    vPaRespeexfloat10.grid(row=1,column=4)

	# Set the Resample value to medium for variable vPaRe
    vPaRemedium=Radiobutton(frame5,indicatoron=0,text='medium',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = src-sinc-medium-quality',command=PaRe,width=16)
    vPaRemedium.grid(row=1,column=5)

	# Set the Resample value to best for variable vPaRe
    vPaRebest=Radiobutton(frame5,indicatoron=0,text='best',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = src-sinc-best-quality',command=PaRe,width=16)
    vPaRebest.grid(row=1,column=6)

	# Set the Resample value to zero-orderhold for variable vPaRe
    vPaRezeroOrderhold=Radiobutton(frame5,indicatoron=0,text='zero-orderhold',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = src-zero-order-hold',command=PaRe,width=16)
    vPaRezeroOrderhold.grid(row=1, column=7)

	# Set the Resample value to Default Resampling for variable vPaRe
    vPaReStopResampling=Radiobutton(frame5,indicatoron=0,text='Default Resampling',font=('Monospace Regular',11),variable=vPaRe,value='; resample-method = speex-float-1',command=PaRe,width=26)
    vPaReStopResampling.grid(row=2,column=1,sticky='ew')

	# Set the Resample value to ffmpeg for variable vPaRe
    vPaReffmpeg=Radiobutton(frame5,indicatoron=0,text='ffmpeg',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = ffmpeg',command=PaRe,width=16)
    vPaReffmpeg.grid(row=2,column=4)

	# Set the Resample value to src-linear for variable vPaRe
    vPaResrclinear=Radiobutton(frame5,indicatoron=0,text='src-linear',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = src-linear',command=PaRe,width=16)
    vPaResrclinear.grid(row=2,column=5)

	# Set the Resample value to soxr-hq for variable vPaRe
    vPaResoxrhq=Radiobutton(frame5,indicatoron=0,text='soxr-hq',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = soxr-hq',command=PaRe,width=16)
    vPaResoxrhq.grid(row=2,column=6)

	# Set the Resample value to soxr-vhq for variable vPaRe
    vPaResoxrvhq=Radiobutton(frame5,indicatoron=0,text='soxr-vhq',font=('Monospace Regular',11),variable=vPaRe,value='  resample-method = soxr-vhq',command=PaRe,width=16)
    vPaResoxrvhq.grid(row=2,column=7)

# End ----------

	# Set the Buttons (Default Settings)
    frame6=LabelFrame(page1)
    frame6.grid(row=12,column=0,sticky='NESW')

# ---------- Default & Apply PA Button ----------


# Text below app
    label = Label(frame6, text="     Restarting services take few seconds     ",font=('Monospace Regular',11))
    label.grid(row=1, column=3)

    RemPa12=LabelFrame(frame6,text=" 5) Apply changes ",font=('Monospace Regular',11))
    RemPa12.grid(row=1,column=4,sticky='NES',padx=5,pady=5)

    apply_btn2=Button(RemPa12,text='Apply & Restart PulseAudio',font=('Monospace Regular',11),command=applyPA)
    apply_btn2.grid(row=1,column=1,padx=5,pady=5,sticky='NESW')

# End ----------

    RemPa14=LabelFrame(frame6,text=" * Predefined PulseAudio Config ",font=('Monospace Regular',11))
    RemPa14.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)

    vPaConf01=Radiobutton(RemPa14,text='Default',font=('Monospace Regular',11),variable=vPaPrefConf,value='Default',command=defpa)
    vPaConf01.grid(row=1,column=1,padx=5,sticky='NW')

    vPaConf02=Radiobutton(RemPa14,text='Recommended',font=('Monospace Regular',11),variable=vPaPrefConf,value='Recommended',command=recpa)
    vPaConf02.grid(row=2,column=1,padx=5)

# Button Show Samplerate

    apply_btn3=Button(frame1,text='PulseAudio Status & Output (Click to refresh)',font=('Monospace Regular',11),command=showsamplerate)
    apply_btn3.grid(row=0,column=3)

# -------------------- Tab 2 (ALSA) --------------------

    # page2 main frame
    frame222=tkinter.LabelFrame(page2,bd=6,bg="green3")
    frame222.grid(row=0,column=1,columnspan=10,sticky='NESW')

    # page frame
    frame33=tkinter.LabelFrame(frame222,bd=5,bg="black")
    frame33.grid(row=0,column=1,rowspan=10,sticky='NESW')

	# ALSA conf info frame (white)
    frame122=Label(frame222)
    frame122.grid(row=1,column=1,columnspan=2,sticky='nes',padx=5,pady=5)


    frame101=tkinter.LabelFrame(page2,text='2) Apply changes')
    frame101.grid(row=1,column=10,sticky='NES',padx=5,pady=5)

    frame102=tkinter.LabelFrame(page2,text='1) Select Card')
    frame102.grid(row=1,column=1,sticky='NSW',padx=5,pady=5)



# End ----------

    label=Label(frame33,bg="black",text="------------------------------------------------------------------",font=('Monospace Regular',11))
    label.grid(row=0,column=1,columnspan=10,sticky='nsw')

    # ---------- Show Device Info ----------

    # Show Devices number
    label=Label(frame33,textvariable=vADefDevId,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=0,columnspan=2,sticky='esw')

    # Show Devices name
    label=Label(frame33,textvariable=vADefDevName,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=2,columnspan=2,sticky='esw')

    # Show ALSA Config
    label=Label(frame122,textvariable=ShvALConf,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=5,rowspan=8,columnspan=8,sticky='nes')


    # End ----------

# ---------- ALSA Apply ----------

    try:
        ALSAdevName0=subprocess.check_output(["cat /proc/asound/card0/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName0.set(ALSAdevName0)
    except subprocess.CalledProcessError as e:
        vADefDevName0.set("---")

    try:
        ALSAdevName1=subprocess.check_output(["cat /proc/asound/card1/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName1.set(ALSAdevName1)
    except subprocess.CalledProcessError as e:
        vADefDevName1.set("---")

    try:
        ALSAdevName2=subprocess.check_output(["cat /proc/asound/card2/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName2.set(ALSAdevName2)
    except subprocess.CalledProcessError as e:
        vADefDevName2.set("---")

    try:
        ALSAdevName3=subprocess.check_output(["cat /proc/asound/card3/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName3.set(ALSAdevName3)
    except subprocess.CalledProcessError as e:
        vADefDevName3.set("---")

    try:
        ALSAdevName4=subprocess.check_output(["cat /proc/asound/card4/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName4.set(ALSAdevName4)
    except subprocess.CalledProcessError as e:
        vADefDevName4.set("---")

    try:
        ALSAdevName5=subprocess.check_output(["cat /proc/asound/card5/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName5.set(ALSAdevName5)
    except subprocess.CalledProcessError as e:
        vADefDevName5.set("---")

    try:
        ALSAdevName6=subprocess.check_output(["cat /proc/asound/card6/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName6.set(ALSAdevName6)
    except subprocess.CalledProcessError as e:
        vADefDevName6.set("---")

    try:
        ALSAdevName7=subprocess.check_output(["cat /proc/asound/card7/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName7.set(ALSAdevName7)
    except subprocess.CalledProcessError as e:
        vADefDevName7.set("---")

    try:
        ALSAdevName8=subprocess.check_output(["cat /proc/asound/card8/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName8.set(ALSAdevName8)
    except subprocess.CalledProcessError as e:
        vADefDevName8.set("---")


    OPTIONS = [
    vADefDevName0.get(),
    vADefDevName1.get(),
    vADefDevName2.get(),
    vADefDevName3.get(),
    vADefDevName4.get(),
    vADefDevName5.get(),
    vADefDevName6.get(),
    vADefDevName7.get(),
    vADefDevName8.get()
    ]

    variable01 = StringVar(frame101)
    variable01.set(OPTIONS[0]) # default value

    FindAL01=OptionMenu(frame102, variable01, *OPTIONS )
    FindAL01.grid(row=1,column=0,sticky='nsw')

    def optionsupdate():

        # clear optionmenu
        FindAL01['menu'].delete(0, 'end')

        try:
            ALSAdevName0=subprocess.check_output(["cat /proc/asound/card0/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName0.set(ALSAdevName0)
        except subprocess.CalledProcessError as e:
            vADefDevName0.set("---")

        try:
            ALSAdevName1=subprocess.check_output(["cat /proc/asound/card1/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName1.set(ALSAdevName1)
        except subprocess.CalledProcessError as e:
            vADefDevName1.set("---")

        try:
            ALSAdevName2=subprocess.check_output(["cat /proc/asound/card2/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName2.set(ALSAdevName2)
        except subprocess.CalledProcessError as e:
            vADefDevName2.set("---")

        try:
            ALSAdevName3=subprocess.check_output(["cat /proc/asound/card3/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName3.set(ALSAdevName3)
        except subprocess.CalledProcessError as e:
            vADefDevName3.set("---")

        try:
            ALSAdevName4=subprocess.check_output(["cat /proc/asound/card4/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName4.set(ALSAdevName4)
        except subprocess.CalledProcessError as e:
            vADefDevName4.set("---")

        try:
            ALSAdevName5=subprocess.check_output(["cat /proc/asound/card5/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName5.set(ALSAdevName5)
        except subprocess.CalledProcessError as e:
            vADefDevName5.set("---")

        try:
            ALSAdevName6=subprocess.check_output(["cat /proc/asound/card6/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName6.set(ALSAdevName6)
        except subprocess.CalledProcessError as e:
            vADefDevName6.set("---")

        try:
            ALSAdevName7=subprocess.check_output(["cat /proc/asound/card7/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName7.set(ALSAdevName7)
        except subprocess.CalledProcessError as e:
            vADefDevName7.set("---")

        try:
            ALSAdevName8=subprocess.check_output(["cat /proc/asound/card8/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName8.set(ALSAdevName8)
        except subprocess.CalledProcessError as e:
            vADefDevName8.set("---")

        OPTIONS = [
        vADefDevName0.get(),
        vADefDevName1.get(),
        vADefDevName2.get(),
        vADefDevName3.get(),
        vADefDevName4.get(),
        vADefDevName5.get(),
        vADefDevName6.get(),
        vADefDevName7.get(),
        vADefDevName8.get()
        ]

        variable01.set(OPTIONS[0]) # default value

        #new optionmenu

        for choice in OPTIONS:
           FindAL01['menu'].add_command(label=choice, command=tkinter._setit(variable01, choice))


        ALSAdevId=subprocess.check_output([" aplay -l | awk -F \: '/,/{print $1}' | uniq "],universal_newlines=True,shell=True).strip();
        vADefDevId.set(ALSAdevId)

        ALSAdevName=subprocess.check_output(["aplay -l | awk -F \: '/,/{print $2}' | awk '{print $1}' | uniq"],universal_newlines=True,shell=True).strip();
        vADefDevName.set(ALSAdevName)
        subprocess.call('echo "-----------------------------------------------------------" && echo " Detected Soundcards \n"-----------------------------------------------------------""', shell=True)
        print (vADefDevName.get())


    # Button Show Devices
    FindAL=Button(frame33,text='Detect Soundcards',command=optionsupdate)
    FindAL.grid(row=0,column=0,columnspan=9,rowspan=1,padx=5,pady=5,sticky='nsw')

    # User inputbox
    frame4=Label(frame101)
    frame4.grid(row=1,column=1,sticky='NESW')

    def applyalsa():
        print(variable01.get())
        Cappterminal=(variable01.get())
        subprocess.call('sudo sed -i "/card / c card {}" /etc/asound.conf'.format(Cappterminal),shell=True);

        ALSAConf=subprocess.check_output(["cat /etc/asound.conf"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        ShvALConf.set(ALSAConf)

        subprocess.call('alsactl kill rescan && alsactl nrestore ',stderr=subprocess.DEVNULL, shell=True)
        subprocess.call('echo "-----------------------------------------------------------" && echo " Current /etc/asound.conf file \n"-----------------------------------------------------------""', shell=True)
        subprocess.call('cat /etc/asound.conf', shell=True)


    apply_btn3=Button(frame101,text='Apply & Restart Alsa',font=('Monospace Regular',11),command=applyalsa)
    apply_btn3.grid(row=1,column=1,sticky='nesw')


# End ----------

# -------------------- Tab 3 (Config) --------------------

    # Tab3 main frame
    CMainP=tkinter.LabelFrame(page3, text=" Installer ")
    CMainP.grid(row=1,column=1,columnspan=7,rowspan=5,sticky='NESW')

    RemPa111=tkinter.LabelFrame(CMainP,text=" PulseAudio (Experimental) ")
    RemPa111.grid(row=1,column=1,sticky='NESW')

    RemPa1111=tkinter.LabelFrame(CMainP,text=" ALSA Compatible Browser ")
    RemPa1111.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)


# ---------- Remove PulseAudio ----------

	# Select to install PulseAudio
    RadPul01=Radiobutton(RemPa111,text='Install PulseAudio',variable=vPaInst,value=' Install PulseAudio')
    RadPul01.grid(row=1,column=1,sticky='NESW')

	# Select to uninstall PulseAudio
    RadPul02=Radiobutton(RemPa111,text='Uninstall PulseAudio',variable=vPaInst,value=' Uninstall PulseAudio')
    RadPul02.grid(row=1,column=2,sticky='NESW')

    RemPa12=tkinter.LabelFrame(RemPa111)
    RemPa12.grid(row=2,column=1,columnspan=4,sticky='NESW')

    label=Label(RemPa12,text="INSTALL Replaces lxde with lubuntu-desktop")
    label.grid(row=3,column=1,columnspan=10,sticky='nsw')

    # Separator5
    # ttk.Separator(RemPa12).grid(row=4,column=1,sticky="ew")

    label=Label(RemPa12,text="UNINSTALL Replaces lubuntu-desktop with lxde")
    label.grid(row=5,column=1,columnspan=10,sticky='nsw')

    # Separator
    ttk.Separator(RemPa12).grid(row=6,column=1,sticky="ew")

    label=Label(RemPa12,text="System will reboot after install")
    label.grid(row=7,column=1,columnspan=10,sticky='nsw')

    AplPul1=Button(RemPa111,text='Apply',command=installerPA)
    AplPul1.grid(row=8,column=1,columnspan=4,padx=5,sticky='NESW')

# End ----------

# ---------- Install Palemoon Browser ----------

	# Select to install Chromium
    RadAL01=Radiobutton(RemPa1111,text='Install Chromium',variable=vBrowserInst,value=' Install Chromium')
    RadAL01.grid(row=1,column=0,sticky='nsw')

	# Select to uninstall Chromium
    RadAL02=Radiobutton(RemPa1111,text='Uninstall Chromium',variable=vBrowserInst,value=' Uninstall Chromium')
    RadAL02.grid(row=1,column=1,sticky='nsw')

	# Select to install Firefox ESR
    RadAL03=Radiobutton(RemPa1111,text='Install Firefox ESR',variable=vBrowserInst,value=' Install Firefox ESR')
    RadAL03.grid(row=2,column=0,sticky='nsw')

	# Select to uninstall Firefox ESR
    RadAL04=Radiobutton(RemPa1111,text='Uninstall Firefox ESR',variable=vBrowserInst,value=' Uninstall Firefox ESR')
    RadAL04.grid(row=2,column=1,sticky='nsw')

	# Select to install Palemoon

    RadAL05=Radiobutton(RemPa1111,text='Install Pale Moon',variable=vBrowserInst,value=' Install Palemoon')
    RadAL05.grid(row=3,column=0,sticky='nsw')

	# Select to uninstall Palemoon
    RadAL06=Radiobutton(RemPa1111,text='Uninstall Pale Moon',variable=vBrowserInst,value=' Uninstall Palemoon')
    RadAL06.grid(row=3,column=1,sticky='nsw')

	# Select to install Firefox
    RadAL03=Radiobutton(RemPa1111,text='Install Firefox (Not Compatible)',variable=vBrowserInst,value=' Install Firefox')
    RadAL03.grid(row=5,column=0,sticky='nsw')

	# Select to uninstall Firefox
    RadAL04=Radiobutton(RemPa1111,text='Uninstall Firefox (Not Compatible)',variable=vBrowserInst,value=' Uninstall Firefox')
    RadAL04.grid(row=5,column=1,sticky='nsw')

    AplAL1=Button(RemPa1111,text='Apply',command=cBrowserInst)
    AplAL1.grid(row=6,column=1,padx=5,pady=5,sticky='NESW')

# End ----------

    top.mainloop()

# ---------- Variable Config ----------

# PulseAudio
vPaBitdepth=StringVar() 			# BithDepth
vPaPriRate=StringVar() 				# Primary Samplerate
vPaAltRate=StringVar() 				# Alternative Samplerate
vPaRe=StringVar() 				# Resample method
vPaRun=StringVar()                  		# Check Running PulseAudio instances
vPaPrefConf=StringVar()             		# Predefined Conf

ShvPaOut=StringVar() 				# Show Current PA output

# ALSA
ShvALConf=StringVar()                   # Alsa asound.conf file data
vADefDev=StringVar() 			    	# Default Device
vADefDevId=StringVar()                  # Device id
vADefDevName=StringVar() 		    	# Device name list

vADefDevName0=StringVar() 		    	# Device name list
vADefDevName1=StringVar() 		    	# Device name list
vADefDevName2=StringVar() 		    	# Device name list
vADefDevName3=StringVar() 		    	# Device name list
vADefDevName4=StringVar() 		    	# Device name list
vADefDevName5=StringVar() 		    	# Device name list
vADefDevName6=StringVar() 		    	# Device name list
vADefDevName7=StringVar() 		    	# Device name list
vADefDevName8=StringVar() 		    	# Device name list


# Installers
vPaInst=StringVar()                		# Install/Uninstall PulseAudio
vBrowserInst=StringVar()               		# Install Palemoon

# End ----------

# ---------- Set some Values for Variable on app startup ----------

# PulseAudio
vPaBitdepth.set('; default-sample-format = s16le')      # PulseAudio BithDepth
vPaPriRate.set('; default-sample-rate = 44100')         # PulseAudio Primary Samplerate
vPaAltRate.set('; alternate-sample-rate = 48000')       # PulseAudio Alternative Samplerate
vPaRe.set('; resample-method = speex-float-1')          # PulseAudio Resample method
vPaRun.set('')                                          # Check Running PulseAudio instances
vPaPrefConf.set('')                                     # Predefined Conf initial value
ShvPaOut.set('')                                        # Show Current PA output

# ALSA
vADefDev.set('') 		                        # ALSA Default Device
vADefDevName.set('') 		                        # ALSA Default name list

# Installers
vPaInst.set('0')                                        # Install/Uninstall PulseAudio
vBrowserInst.set('0')                                      # Install browser


# ---------- Print Variable Data ----------

# PulseAudio
def Pabitdepth():
    print(vPaBitdepth.get())

def PaPriRate():
    print(vPaPriRate.get())

def PaAltRate():
    print(vPaAltRate.get())

def PaRe():
    print(vPaRe.get())

def PaOut():
    print(ShvPaOut.get())

def PaRun():
    print(vPaRun.get())

def PaPrefConf():
    print(vPaPrefConf.get())

# ALSA
def ADefDev():
    print(vADefDev.get())

# Installers
def PaInst():
    print(vPaInst.get())

def BrowserInst():
    print(vBrowserInst.get())

# End ----------

# ---------- Button Commands ----------

def helpmenu01():
    tkinter.messagebox.showinfo("About Audio Powertool: ","Easy audio settings management\n \nNo more boring Config files\n \n")

# Default button
def defpa():
# Set new values for variables
    vPaBitdepth.set('; default-sample-format = s16le')
    vPaPriRate.set('; default-sample-rate = 44100')
    vPaAltRate.set('; alternate-sample-rate = 48000')
    vPaRe.set('; resample-method = speex-float-1')
    print (" Default Values ")
# End ----------

def recpa():
# Set new values for variables
    vPaBitdepth.set('  default-sample-format = s24le')
    vPaPriRate.set('  default-sample-rate = 44100')
    vPaAltRate.set('  alternate-sample-rate = 48000')
    vPaRe.set('; resample-method = speex-float-1')
    print (" Recommended Values ")
# End ----------


# Apply PA Button
def applyPA():
    CvPaBitdepth=(vPaBitdepth.get())
    CvPaPriRate=(vPaPriRate.get())
    CvPaAltRate=(vPaAltRate.get())
    CvPaRe=(vPaRe.get())

    subprocess.call('sudo sed -i "/default-sample-format =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/default-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/alternate-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/resample-method =/ c {}" /etc/pulse/daemon.conf | pulseaudio --kill ; pulseaudio --start'.format(CvPaBitdepth,CvPaPriRate,CvPaAltRate,CvPaRe),shell=True);

# The current PulseAudio output setting is passed to variable and printed to terminal
def showsamplerate():
    try:
        showsamplerateoutput=subprocess.check_output(["pacmd list-sinks | grep sample"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        ShvPaOut.set(showsamplerateoutput)
        PaStatus=subprocess.check_output(["pulseaudio --check"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        vPaRun.set("Status: On")
        print ("---------------- PulseAudio -----------------")
        print (vPaRun.get())
        print (ShvPaOut.get())
        print ("---------------------------------------------")
    except subprocess.CalledProcessError as e:
        ShvPaOut.set("Output: N/A")
        vPaRun.set("Status: Off")
        print ("---------------- PulseAudio -----------------")
        print (vPaRun.get())
        print (ShvPaOut.get())
        sys.stderr.write(
        "No PulseAudio playback detected: %s\n"
        % (e.returncode))
        print ("---------------------------------------------")
# End ----------

# Apply Alsa
def applyAL():
    cADefDev=(vADefDev.get())
    cADefDev=(vADefDev.get())

    subprocess.call('sudo sed -i "/card / c card {}" /etc/asound.conf && sudo sed -i "/card / c card {}" /etc/asound.conf | alsactl kill rescan && alsactl nrestore'.format(cADefDev,cADefDev),shell=True);

# Uninstall/install PulseAudio
def installerPA():
    PaInst=(vPaInst.get())
    if PaInst==" Install PulseAudio":
        print ("-------------- Install PulseAudio --------------")
        subprocess.call('sudo apt purge --remove lubuntu-* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt purge --remove lxde* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt-get install lubuntu-desktop -y',shell=True);
        subprocess.call('sudo apt-get install alsa-base pulseaudio -y',shell=True);
        subprocess.call('sudo alsa force-reload',shell=True);
        subprocess.call('pulseaudio --kill ; pulseaudio --start',shell=True);

        subprocess.call('sudo apt-get update',shell=True);
        subprocess.call('sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt-get autoclean -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")
        subprocess.call('sleep 1 && echo "System Reboot in..." && sleep 1 && echo "3" && sleep 1 && echo "2" && sleep 1 && echo "1" && sleep 1 && sudo reboot',shell=True);

    if PaInst==" Uninstall PulseAudio":
        print ("-------------- Uninstall PulseAudio --------------")
        subprocess.call('pulseaudio -k | killall pulseaudio',shell=True);

	# Uninstall -->
        subprocess.call('sudo apt purge --remove pulseaudio* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt purge --remove padevchooser* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt purge --remove pavucontrol* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt purge --remove paprefs* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt-get purge gstreamer0.10-pulseaudio -y',shell=True);
        subprocess.call('sudo apt-get purge alsa-base -y',shell=True);
#        subprocess.call('sudo apt purge unity-session unity -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt purge --remove lubuntu-* -y; sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt purge --remove lxde* -y; sudo apt autoremove -y',shell=True);

	# New Desktop Env
        subprocess.call('sudo apt-get install lxde -y',shell=True);
        subprocess.call('sudo apt install lxde-common -y',shell=True);

	# Cleanup & Reboot
        subprocess.call('sudo apt-get update',shell=True);
        subprocess.call('sudo apt autoremove -y',shell=True);
        subprocess.call('sudo apt-get autoclean -y',shell=True);
        subprocess.call('sudo apt-get install alsa -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")
        subprocess.call('sleep 1 && echo "System Reboot in..." && sleep 1 && echo "3" && sleep 1 && echo "2" && sleep 1 && echo "1" && sleep 1 && sudo reboot',shell=True);

# End ----------

# install Palemoon
def cBrowserInst():
    vdBrowserInst=(vBrowserInst.get())

    if vdBrowserInst==" Install Chromium":
        print ("-------------- Install Chromium --------------")
        subprocess.call('sudo apt-get install chromium-browser -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Uninstall Chromium":
        print ("-------------- Uninstall Chromium --------------")
        subprocess.call('sudo apt-get purge chromium-browser -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Install Firefox ESR":
        print ("-------------- Install Firefox ESR --------------")
        subprocess.call('sudo add-apt-repository ppa:mozillateam/ppa -y && sudo apt-get update && sudo apt-get install firefox-esr -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Uninstall Firefox ESR":
        print ("-------------- Uninstall Firefox ESR --------------")
        subprocess.call('sudo apt-get remove --auto-remove firefox-esr -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Install Firefox":
        print ("-------------- Install Firefox --------------")
        subprocess.call('sudo apt-get install firefox -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Uninstall Firefox":
        print ("-------------- Uninstall Firefox ESR --------------")
        subprocess.call('sudo apt-get remove --auto-remove firefox -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Install Palemoon":
        print ("-------------- install Palemoon --------------")
        subprocess.call('wget -nv https://download.opensuse.org/repositories/home:stevenpusser/xUbuntu_18.04/Release.key -O Release.key',shell=True);
        subprocess.call('sudo apt-key add - < Release.key && sudo apt-get update',shell=True);
        BrowserInst1=("sudo sh -c")
        BrowserInst2=("'deb http://download.opensuse.org/repositories/home:/stevenpusser/xUbuntu_16.04/ /'")
        subprocess.call('{} "echo {} > /etc/apt/sources.list.d/home:stevenpusser.list"'.format(BrowserInst1,BrowserInst2),shell=True);
        subprocess.call('sudo apt-get update',shell=True);
        subprocess.call('sudo apt-get install palemoon -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

    if vdBrowserInst==" Uninstall Palemoon":
        print ("-------------- Uninstall Palemoon --------------")
        subprocess.call('sudo rm /etc/apt/sources.list.d/home:stevenpusser.list',shell=True);
        subprocess.call('sudo apt-get purge palemoon -y',shell=True);
        print ("--------------------------------------------")
        print (" Done !")

# End ----------


# The current ALSA device list is passed to variable and printed to terminal
def showalsadevices():

    ALSAdevId=subprocess.check_output([" aplay -l | awk -F \: '/,/{print $1}' | uniq "],universal_newlines=True,shell=True).strip();
    vADefDevId.set(ALSAdevId)

    ALSAdevName=subprocess.check_output(["aplay -l | awk -F \: '/,/{print $2}' | awk '{print $1}' | uniq"],universal_newlines=True,shell=True).strip();
    vADefDevName.set(ALSAdevName)
    subprocess.call('echo "-----------------------------------------------------------" && echo " Detected Soundcards \n"-----------------------------------------------------------""', shell=True)
    print (vADefDevName.get())


# End ----------

# Run at start to check --> asound.conf exist and if not it will be created (config file creation will fail if app is not run with sudo. Alternatively config can be created manually by following this tutorial --> https://www.alsa-project.org/main/index.php/Setting_the_default_device)
try:
    subprocess.check_output(["cat /etc/asound.conf"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
except subprocess.CalledProcessError as e:
    subprocess.call('echo "-----------------------------------------------------------" && echo " Creating SystemWide asound.conf file \n"-----------------------------------------------------------""', shell=True)
    subprocess.call('[ -f /etc/asound.conf ] && echo "------------------------ ALSA Conf ------------------------" || echo "pcm.!default {\ntype hw\ncard "1"\n} \nctl.!default {\ntype hw\ncard "1"\n}" > /etc/asound.conf', shell=True)
    subprocess.call('alsactl kill rescan && alsactl nrestore ', stderr=subprocess.DEVNULL,shell=True)

ALSAConf=subprocess.check_output(["cat /etc/asound.conf"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
ShvALConf.set(ALSAConf)

# Close Window
def close_window():
    root.destroy()
    root.mainloop()
# End ----------

if __name__ == '__main__':
    main()
