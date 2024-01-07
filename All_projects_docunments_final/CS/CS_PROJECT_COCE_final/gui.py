from tkinter import *
from tkinter import messagebox
import oxilanari_functions as oxi
import functions_project as f_p
import graph_function as g_p 

oxi_info = oxi.get_function_name()
oxi_gra_info = oxi.get_graph_function_name()

global win
win = Tk()
win.configure(bg = 'light green')
win.title('CS project')
win.geometry('600x600')
win.resizable(0,0)

fram_intro = None
fram_for = None
fram_gra_con = None
fram_add_f_g = None
fram_run_fun = None
fram_graph = None
ans = 0
el = None
l_ans = None
n_list_v = list(oxi_info)
d = 0
v = ''


def run_fun(name):
    global n_list_v
    global ans
    global el
    global l_ans
    global v
    n_list_v = []

    def find_ans():
        global ans
        global el
        global l_ans
        global v
        if el != None:
            el.destroy()
        x = None
        e = '('
        for i in range(len(v[1])):
            e += ev[i].get() + ','
        e = e[:-1:]
        e += ')'
        for i in oxi_info:
            if i[0] == name:
                x = i[1]
                break
        try:
            ans = eval('f_p.'+x[:x.index('(')]+e)[1]
        except ZeroDivisionError:
            messagebox.showerror('Zero Division Error','enter values which very near to zero so that effectively finding limit of that at zero')
            return None
        except ValueError:
            messagebox.showerror('Value Error','Enter value in its range')
            return None
        except:
            messagebox.showerror('Value Error','Enter currect value')
            return None
        if l_ans != None:
            l_ans.destroy()
        l_ans = Label(fram_run_fun,text = f"Answer is {v[0][:v[0].index('=')+1]}{ans}",font = ('Times New Roman',15))
        l_ans.grid(row = u+2,column = 0)
    def check_run_fun():
        a = True
        z = 0
        global el
        global l_ans
        for i in ev:
            if len(i.get()) == 0:
                messagebox.showerror('sujection to error','enter all values')
                a = False
                break
            else:
                try:
                    float(i.get())
                except ValueError:
                    messagebox.showerror('sujection to error','enter all values with no alphabets or spectal charactor')
                    a = False
                    break
            
        if a:
            find_ans()

    global fram_for
    global fram_run_fun
    fram_for.destroy()
    fram_run_fun = Frame(win)
    fram_run_fun.pack()

    for i in oxi_info:
        if i[0] == name:
            v = oxi.run_and_return_function_formula_var(i[1])
            break
    g = Label(fram_run_fun,text = 'Formula '+v[0],font = ('Times New Roman',15))
    g.grid(row = 0,column= 0)
    Label(fram_run_fun,text = '',font = ('Times New Roman',15),pady = 10).grid(row = 1,column= 0)
    ev = []
    s = 0
    u = 3
    for i in range(len(v[1])):
        ev.append(Entry(fram_run_fun,font = ('Times New Roman',15)))
        
    for i in ev:
        Label(fram_run_fun,text = f"enter the value of variable {v[1][s]}",font = ('Times New Roman',15)).grid(row = u-1,column = 0)
        i.grid(row = u,column = 0)
        Label(fram_run_fun,text = '',font = ('Times New Roman',15),pady = 5).grid(row = u+1,column= 0)
        u += 3
        s += 1
    k = Button(fram_run_fun,text = 'calculate',command = check_run_fun,font = ('Times New Roman',15))
    k.grid(row = u+1,column= 0)
    Label(fram_run_fun,text = '',pady = 10).grid(row = u+2,column = 0)
    h = Button(fram_run_fun,text = 'Back',command = view_for,font = ('Times New Roman',15))
    h.grid(row = u+4,column= 0)
    Label(fram_run_fun,text = '',pady = 150).grid(row = u+5,column = 0)

def intro():
    global fram_intro
    global fram_for
    global fram_gra_con
    global fram_
    global fram_run_fun

    if fram_for != None:
        fram_for.destroy()
    if fram_gra_con != None:
        fram_gra_con.destroy()
    if fram_add_f_g != None:
        fram_add_f_g.destroy()

    fram_intro = Frame(win)
    fram_intro.pack()
    Label(fram_intro,text = 'physics numerical solver'.upper(),font = ('Times New Roman',20,'bold'),fg = '#F68C22').grid(row = 0,column = 1,pady = 100,padx = 30)
    Label(fram_intro,text = '',pady = 35).grid(row = 1,column = 1)
    but_for = Button(fram_intro,text = 'view formula to solve',command = view_for,font=('Times New Roman',17),bg = 'light blue')
    but_for.grid(row = 2,column = 1,padx = 40,pady = 10)
    but_gr_ap = Button(fram_intro,text = 'graph and real life applications',command = view_gra_con,font=('Times New Roman',17),bg = 'light blue')
    but_gr_ap.grid(row = 3,column = 1,padx = 40,pady = 10)
    but_hello = Button(fram_intro,text = 'Add formula',command = add_fun_gra,font=('Times New Roman',17),bg = 'light blue')
    but_hello.grid(row = 4,column = 1,padx = 40,pady = 10)
    Label(fram_intro,text='').grid(row = 5,column = 1,pady=50)

def view_for():
    global n_list_v
    def abc():
        if list_box.get(ANCHOR) != '':
            run_fun(list_box.get(ANCHOR))
        else:
            messagebox.showerror('sujection to error','select any forrmula to work')

    def sca():
        global n_list_v
        n_list_v = []
        nm = 0
        for i in oxi_info:
            list_box.delete(0,END)
            if len(s_e.get()) != 0:
                if s_e.get().lower() in i[0].lower():
                    n_list_v.append((i[0]))
            else:
                n_list_v.append((i[0]))
        for i in n_list_v:
            list_box.insert(END,i)


    global v
    global fram_for
    global fram_run_fun
    fram_intro.destroy()
    if fram_run_fun != None:
        fram_run_fun.destroy()
    fram_for = Frame(win)
    fram_for.pack()
    Label(fram_for,text = 'View Formula',pady = 0,font = ('Times New Roman',20)).grid(row = 0,column = 1,pady = 10)
    Label(fram_for,text = 'Search Formula ',font = ('Times New Roman',15)).grid(row = 1,column = 0)
    s_e = Entry(fram_for,width=30,font = ('Times New Roman',13))
    s_e.grid(row = 1,column = 1)
    Button(fram_for,text = 'Search',command = sca,font = ('Times New Roman',13)).grid(row = 1,column = 3)
    list_box = Listbox(fram_for,width = 80,height = 25,font = ('Times New Roman',10))
    list_box.grid(row = 2,column = 0,columnspan = 4)
    if len(n_list_v) == 0:
        n_list_v = oxi_info
    for i in n_list_v:
        try:
            list_box.insert(END,i[0])
        except:
            pass
    Button(fram_for,text = 'Select',command = abc,font = ('Times New Roman',13)).grid(row = 3,column = 0)
    Button(fram_for,text = 'Back',command = intro,font = ('Times New Roman',13),padx = 30).grid(row = 4,column = 3)
    Label(fram_for,text = '',pady = 55).grid(row = 5,column = 0)

def graph(f):
    global d,list_box_gra,fram_graph
    def abcdefghij():
        global d
        s = '('
        for i in range(len(vg[0])):
            s += str(el[i].get()) + ','
        s = s[:-1]
        s += ')'
        d = d.replace(d[d.index('('):],s)
        try:
            eval('g_p.'+d)
        except ZeroDivisionError:
            messagebox.showerror('Zero Division Error','Enter non zero ractional values')
            return None
        except:
            messagebox.showerror('Sujection to error','Enter currect values')
            return None
    
    def check_run_graph():
        a = True
        for i in el:
            if len(i.get()) == 0:
                messagebox.showerror('sujection to error','enter all values')
                a = False
                break
            else:
                for j in i.get():
                    try:
                        float(j)
                    except ValueError:
                        messagebox.showerror('sujection to error','enter all values with no alphabets or spectal charactor')
                        a = False
                        break
            
        if a:
            abcdefghij()
    
    fram_gra_con.destroy()
    fram_graph = Frame(win)
    fram_graph.pack()
    vg = list()
    el = list()
    r = 1
    d = 0
    for i in oxi_gra_info:
        if i[0] == f:
            d = i[1]
            vg.append(i[1][i[1].index('(')+1:i[1].index(')')].split(','))
            vg.append(i)
    for i in range(len(vg[0])):
        Label(fram_graph,text = "",pady=10).grid(row = r-1,column = 0)
        Label(fram_graph,text = f"enter the value of {vg[0][i]}",font=('Times New Roman',20),padx=100).grid(row = r,column = 0)
        a = Entry(fram_graph,font=('Times New Roman',20))
        a.grid(row = r+1,column = 0)
        el.append(a)
        r += 3
    Label(fram_graph,text = "",pady=20).grid(row = r-1,column = 0)
    Button(fram_graph,text = 'Draw Graph',command = check_run_graph,font=('Times New Roman',15),padx = 30).grid(row = r,column = 0)
    Label(fram_graph,text = "",pady=20).grid(row = r+1,column = 0)
    Button(fram_graph,text = 'Back',command = view_gra_con,font=('Times New Roman',15),padx = 30).grid(row = r+2,column = 0)
    Label(fram_graph,text = "",pady=50).grid(row = r+3,column = 0)

def view_gra_con():
    def check_select_gra():
        if len(list_box_gra.get(ANCHOR)) != 0:
            graph(list_box_gra.get(ANCHOR))
        else:
            messagebox.showerror('sujection to error','select any graph')

    global fram_gra_con
    global list_box_gra
    if fram_intro != None:
        fram_intro.destroy()
    if fram_graph != None:
        fram_graph.destroy()
    fram_gra_con = Frame(win)
    fram_gra_con.pack()
    Label(fram_gra_con,text = 'View Graph',pady = 0,font=('Times New Roman',17)).grid(row = 0,column = 1)
    list_box_gra = Listbox(fram_gra_con,width = 50,height = 17,font=('Times New Roman',15))
    list_box_gra.grid(row = 1,column = 0,columnspan = 4)
    for i in oxi_gra_info:
        list_box_gra.insert(END,i[0])
    Button(fram_gra_con,text = 'View Graph',font=('Times New Roman',13),padx=15,command = check_select_gra).grid(row = 2,column = 0)
    Button(fram_gra_con,text = 'Back',command = intro,font=('Times New Roman',13),padx = 20).grid(row = 3,column = 3)
    Label(fram_gra_con,text='',pady = 50).grid(row = 4,column = 0)

def add_fun_gra():
    t = '''
1. The formula must have name to acess this formula
2. The Symbolic representation of equation in math shoud be converted to python gets no error
3. All variables must be listed in the variable intry to avoid error
'''
    messagebox.showinfo('Things to consider for adding formula',t)
    global fram_add_f_g
    if fram_intro != None:
        fram_intro.destroy()
    
    def ADD():
        try:
            oxi.add_for(e_fn.get(),e_fo.get(),e_fv.get())
        except:
            pass
    
    fram_add_f_g = Frame(win)
    fram_add_f_g.pack()
    Label(fram_add_f_g,text = 'Add formula',pady = 0,font = ('times new roman',20)).grid(row = 0,column = 0,columnspan=2)
    Label(fram_add_f_g,text = '',pady = 10).grid(row = 1,column = 0)

    Label(fram_add_f_g,text = 'Enter formula name',font = ('times new roman',17)).grid(row = 2,column = 0)
    e_fn = Entry(fram_add_f_g,font = ('times new roman',15),width=30)
    e_fn.grid(row = 3,column = 0)

    Label(fram_add_f_g,text = 'Enter Formula',font = ('times new roman',17)).grid(row = 4,column = 0)
    e_fo = Entry(fram_add_f_g,font = ('times new roman',15),width=30)
    e_fo.grid(row = 5,column = 0)

    Label(fram_add_f_g,text = 'Enter all the variable with a speace',font = ('times new roman',17)).grid(row = 6,column = 0)
    e_fv = Entry(fram_add_f_g,font = ('times new roman',15),width=30)
    e_fv.grid(row = 7,column = 0)

    Label(fram_add_f_g,text = '',pady = 7).grid(row = 8,column = 0)
    Button(fram_add_f_g,text = 'Add',command = ADD,font = ('times new roman',20)).grid(row = 9,column = 0)
    Label(fram_add_f_g,text = '',pady = 0).grid(row = 10,column = 0)
    Button(fram_add_f_g,text = 'Back',command = intro,font = ('times new roman',20)).grid(row = 11,column = 1)
    Label(fram_add_f_g,text = '',pady = 160).grid(row = 12,column = 0)


intro()
win.mainloop()
