    from tkinter import *
    from tkinter import messagebox as mb
    from tkinter import font
    import ipaddress as ipa
    frame = Tk()
    frame.title("IPv4 Calculator")
    frame.geometry("1280x1000")
    frame.state('zoomed')
    maintitle=Label(frame,text="IPv4 Subnet Calculator",fg="white",bg="cyan4",font=font.Font(family="bold", size=28))
    maintitle.place(x=601,y=-1)

    ipl=Label(frame, text="Enter (IP Address/CIDR notation):", fg="black", font=font.Font(family="Tahoma", size=12))
    ipl.place(x=660, y=50)
    ipe = Entry(frame, font=font.Font(size=20), width=25)
    ipe.place(x=600, y=82)

    ipl=Label(frame, text="Made by @mohammed farnas ali mudabbir", fg="cadetblue4", font=font.Font(family="Tahoma", size=12))
    ipl.place(x=640, y=670)


    ipe = Entry(frame, font=font.Font(size=20), width=25)  #textbox
    ipe.place(x=600, y=82)

    r_frame = Frame(frame,bg="cyan4")
    r_frame.place(x=430, y=135)


    def calculate():
        clear_rframe()
        value = ipe.get()
        try:
            ip, cidr=value.split('/')
            ip_check=ipa.IPv4Address(ip)
            cidr=int(cidr)
            if cidr<1 or cidr>30:
                mb.showwarning("Invalid CIDR", "Please enter a valid CIDR between 1-30")
            else:
                net_add(value)
                subnetmask(cidr)
        except ValueError:
            mb.showwarning('IP Address and CIDR Error', "Enter a valid IP Address with CIDR Notation")
        except ipa.AddressValueError:
            mb.showwarning('IP Address Error', "Enter a valid IP Address")

    def net_add(ip):
        net=ipa.IPv4Network(ip, strict=False)
        net_add_str=str(net.network_address)
        rlabel("NETWORK ADDRESS:",net_add_str)
        host_range(net)
        broadcast_add(net)
        ipclass(ip)


    def broadcast_add(net):
        broad_add=str(net.broadcast_address)
        rlabel("BROADCAST ADDRESS:",broad_add)

    def host_range(net):
        f_host=str(net.network_address+1)
        l_host=str(net.broadcast_address-1)
        total=f"{f_host} - {l_host}"
        rlabel("USABLE HOST RANGE:",total)

    def subnetmask(cidr):
        sm=[]
        for i in range(cidr//8):
            sm.append(255)
        last=0
        for i in range(cidr%8):
            last+=2**(7-i)
        sm.append(last)
        while len(sm) < 4:
            sm.append(0)
        subnet=".".join(map(str,sm))
        rlabel("SUBNET MASK:",subnet)

    def ipclass(ip):
        ip=ip.split('.')
        f_oct=int(ip[0])
        if 1<=f_oct<=126:
            ip_class="A"
        elif 128<=f_oct<=191:
            ip_class="B"
        elif 192<=f_oct<=223:
            ip_class="C"
        elif 224<=f_oct<=239:
            ip_class="D"
        elif 240<=f_oct<=255:
            ip_class="E"
        rlabel("IP CLASS:",ip_class)

    def rlabel(label_text, value):
        reslabel=Label(r_frame,text=label_text,font=font.Font(family="Tahoma", size=22), fg="black",bg="LemonChiffon3")
        reslabel.grid(sticky=W, padx=10, pady=10)

        resvalue=Label(r_frame, text=value, font=font.Font(family="Tahoma", size=20), fg="blue",bg="LemonChiffon3")
        resvalue.grid(row=r_frame.grid_size()[1]-1, column=1, sticky=W, padx=10, pady=10)

    def clear_rframe():
        for widget in r_frame.winfo_children():
            widget.destroy()

    Bt=Button(frame,text="Calculate",command=calculate,fg="white",bg="cyan4",font=font.Font(family="Tahoma", size=16))
    Bt.place(x=740, y=480)

    frame.mainloop()