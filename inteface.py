from tkinter import *
from tkinter.ttk import *
import subprocess


class Interface:
    def __init__(self):
        window = Tk()

        window.title("Change IP address")
        main_frame = Frame(window)
        main_frame.pack()

        # Label 'IP Address' and TextEdit 'IP Address content'
        frame_ip = Frame(main_frame)
        self.lb_ip_addr = Label(frame_ip, text='IP Address:', font=('Helvetica', 16))
        self.ted_ip_addr = Entry(frame_ip, width=50, font=('Helvetica', 12), justify='center')
        self.lb_ip_addr.pack()
        self.ted_ip_addr.pack()
        frame_ip.pack()

        # Label 'Subnet Mask' and TextEdit = 'Subnet Mask content'
        frame_subnet_mask = Frame(main_frame)
        self.lb_subnet_mask = Label(frame_subnet_mask, text='Subnet Mask:', font=('Helvetica', 16))
        self.ted_subnet_mask = Entry(frame_subnet_mask, width=50, font=('Helvetica', 12), justify='center')
        self.lb_subnet_mask.pack()
        self.ted_subnet_mask.pack()
        frame_subnet_mask.pack()

        # Label 'Default Gateway' and TextEdit 'Default Gateway content'
        frame_default_gateway = Frame(main_frame)
        self.lb_default_gateway = Label(frame_default_gateway, text='Default Gateway:', font=('Helvetica', 16))
        self.ted_default_gateway = Entry(frame_default_gateway, width=50, font=('Helvetica', 12), justify='center')
        self.lb_default_gateway.pack()
        self.ted_default_gateway.pack()
        frame_default_gateway.pack()

        # Radio Buttons 'Static' and 'DHCP'
        frame_rds = Frame(main_frame)
        self.rd_variable = StringVar()
        self.rd_variable.set('DHCP')
        self.rd_static = Radiobutton(frame_rds, text='Static', value='Static', variable=self.rd_variable,
                                     command=self.change_ted_state)
        self.rd_dhcp = Radiobutton(frame_rds, text='DHCP', value='DHCP', variable=self.rd_variable,
                                   command=self.change_ted_state)
        self.rd_static.pack(side='left')
        self.rd_dhcp.pack(side='left')
        frame_rds.pack()

        # Button='Change IP'
        frame_button = Frame(main_frame)
        self.button = Button(frame_button, text='Change IP Address', command=self.change_ip)
        frame_button.pack()
        self.button.pack()

        if self.rd_variable.get() == 'DHCP':
            self.ted_ip_addr.config(state='disabled')
            self.ted_subnet_mask.config(state='disabled')
            self.ted_default_gateway.config(state='disabled')

        window.mainloop()

    def change_ted_state(self):
        if self.rd_variable.get() == 'DHCP':
            self.ted_ip_addr.delete(0, END)
            self.ted_ip_addr.config(state='disabled')
            self.ted_subnet_mask.delete(0, END)
            self.ted_subnet_mask.config(state='disabled')
            self.ted_default_gateway.delete(0, END)
            self.ted_default_gateway.config(state='disabled')
        else:
            self.ted_ip_addr.config(state='enabled')
            self.ted_ip_addr.insert(0, '192.169.160.1')
            self.ted_subnet_mask.config(state='enabled')
            self.ted_subnet_mask.insert(0, '255.255.255.224')
            self.ted_default_gateway.config(state='enabled')
            self.ted_default_gateway.insert(0, '192.168.160.1')

    def get_static_variables(self):
        ip_addr = self.ted_ip_addr.get()
        subnet_mask = self.ted_subnet_mask.get()
        default_gateway = self.ted_default_gateway.get()

        with open("static_ip.bat", "r") as bat_file:
            data = bat_file.readlines()

            data[0] = f'set ip_addr={ip_addr}\n'
            data[1] = f'set subnet_mask={subnet_mask}\n'
            data[2] = f'set default_gateway={default_gateway}\n'

        with open("static_ip.bat", "w") as bat_file:
            bat_file.writelines(data)

    def run_bat(self):
        if self.rd_variable.get() == 'Static':
            self.get_static_variables()
            subprocess.call([r'static_ip.bat'], shell=True)
        else:
            subprocess.call([r'dhcp_ip.bat'], shell=True)

    def change_ip(self):
        self.run_bat()
