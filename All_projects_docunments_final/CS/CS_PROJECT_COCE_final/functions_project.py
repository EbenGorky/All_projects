import math
from math import *

def quantization_of_charge__q(n):
	return("Q=",float(n)*(1.6)*(10**-19),"\nFormula:Q=±ne")
def quantization_of_charge_number_of_electrons_in_given_charge__n(Q):
	return("n=",float(Q)/(1.6)*(10**19),"\nFormula:n=Q/e")
def Coulombs_law_Force_between_two_charges__F(q1,q2,r):
	return("F=",float(q1)*float(q2)/((float(r)**2)*9)*(10**9),"N\nFormula:F=k*q1*q2/r**2")
def Coulombs_law_distance_between_two_charges__r(q1,q2,F):
	return("r=",math.sqrt((float(q2)*float(q2)*9)*10**9/float(F)),"m\nFormula:r=(q1*q2*k/F)**1/2")
def Coulombs_law_first_charge__q1(r,q2,F):
	return("q1=",float(r)**2*float(F)/(float(q2)*9*10**9),"C\nFormula:q1=F*r**2/q2*k")
def Coulombs_law_second_charge__q2(q1,r,F):
	return("q2=",float(r)**2*float(F)/(float(q1)*9*10**9),"C\nFormula:q2=F*r**2/q1*k")
def Relation_between_F_and_E__F(q,E):
	return("F=",float(q)*float(E),"N\nFormula:F=qE")
def Relation_between_E_anf_F_Electric_field__E(q,F):
	return("E=",float(F)/float(q),"v/m\nFormula:E=F/q")
def Relation_between_E_and_F_charge__q(E,F):
	return("q=",float(F)/float(E),"C\nFormula:q=F/E")
def Electric_field_due_to_a_point_charge__E(Q,r):
	return("E=",9*float(Q)/float(r)**2*(10**9),"v/m\nFormula:E=k*Q/r**2")
def Electric_field_due_to_a_point_charge_distance_between_charge_and_point__r(Q,E):
	return("r=",math.sqrt((9*10**9)*float(Q)/float(E)),"m\nFormula:r=(k*Q/E)**1/2")
def Electric_field_due_to_a_point_charge_charge__q(r,E):
	return("Q=",(float(E)*float(r)**2)/(9*10**9),"C\nFormula:Q=E*r**2/k")
def Gauss_theorm__phi(q):
	return("phi=",float(q)/8.854*(10**12),"\nFormula:phi=q/epsilon0")
def Gauss_theorem_charge__q(phi):
	return("q=",8.854*float(phi)*(10**-12)," C\nFormula:q=phi*epsilon0")
def Electric_potential_due_to_a_point_charge__V(q,r):
	return("V=",float(q)*9/float(r)*(10**9),"\nFormula:V=k*q/r")
def Electric_potential_due_to_a_point_charge_charge__q(v,r):
	return("q=",(float(v)*float(r))/(9*10**9),"C\nFormula:q=v*r/k")
def Electric_potential_due_to_a_point_charge_distance__r(q,v):
	return("r=",9*10**9*float(q)/float(v),"m\nFormula:r=k*q/V")
def Electric_potential_due_to_dipole__V(p,theta,r):
	return("v=",9*float(p)*math.cos(theta)/(float(r)**2)*10**9,"\nFormula:V=k*p*costheta/r**2")
def Electric_potential_due_to_dipole_distance_between_two_charges__r(p,theta,v):
	return("r=",math.sqrt((9*10**9)*(float(p)*math.cos(float(theta)))/float(v)),"m\nFormula:r=(k*p*costheta/v)**1/2")
def Electric_potential_due_to_dipole_dipole_moment__p(v,r,theta):
	return("p=",float(v)*float(r)**2/(9*10**9*math.cos(float(theta))),"Cm\nFormula:p=v*r**2/k*costheta")
def Electric_potential_due_to_dipole_angle__theta(v,p,r):
	return("theta=",math.acos(((float(v)*10**-9)*(float(r)**2))/9*float(p)),"degree\nFormula:theta=cos**-1(v*r**2/k*p)")
def Potential_energy_of_a_system_of_two_point_charges__U(q1,q2,r):
	return("U=",9*float(q1)*float(q2)/float(r)*(10**9)," J\nFormula:U=k*q1*q2/r")
def Potential_energy_of_a_system_of_two_point_charge_distance_between_two_point_charges__r(q1,q2,U):
	return("r=",(9*10**9)*float(q1)*float(q2)/float(U),"m\nFormula:r=k*q1*q2/U")
def Potential_energy_of_a_system_of_two_point_charge_first_charge__q1(U,r,q2):
	return("q1=",float(U)*float(r)/(9*10**9*float(q2)),"C\nFormula:q1=U*r/k*q2")
def Potential_energy_of_a_system_of_two_point_charge_second_charge__q2(q1,U,r):
	return("q2=",float(U)*float(r)/(9*10**9*float(q1)),"C\nFormula:q2=U*r/k*q1")
def Field_intensity_due_to_infinitely_long_straight_uniformly_charged_wire__E(lamda,R):
	return("E=",float(lamda)/(55.603*(10**-12)*float(R)),"v/m\nFormula:E=lamda/2epsilon0*R")
def Field_intensity_due_to_infinitely_long_straight_uniformly_charged_wire_Resistance__R(lamda,E):
	return("R=",float(lamda)/(55.603*(10**-12)*float(E)),"m\nR=lamda/2pieepsilon0*E")
def Field_intensity_due_to_infinitely_long_straight_uniformly_charged_wire_lamda_value__lamda(R,E):
	return("lamda=",float(R)*55.603*(10**-12)*float(E),"\nFormula:lamda=R*2pieepsilon0*E")
def Field_intensity_due_to_uniformly_charged_spherical_shell_out__E(q,r):
	return("E=",9*float(q)/(float(r)**2)*(10**9),"V/m\nFormula:E=k*q/r**2")
def Field_intensity_due_to_uniformly_charged_spherical_shell_out_radius_of_shell_including_thickness__r(q,E):
	return("r=",math.sqrt(((float(q)*9*10**9)))/math.sqrt(float(E)),"m\nFormula:r=√(q*k/E)")
def Field_intensity_due_to_uniformly_charged_spherical_shell_out_charge__q(E,r):
	return("q=",(float(E)*float(r)**2)/9*(10**-9),"C\nFormula:q=E*r**2/k")
def Field_intensity_due_to_uniformly_charged_spherical_shell_on__E(q,R):
	return("E=",9*float(q)/(float(R)**2 )*(10**9),"V/m\nFormula:E=k*q/R**2")
def Field_intensity_due_to_uniformly_charged_spherical_shell_on_radius_of_shell__r(q,E):
	return("R=",math.sqrt(9*10**9*float(q))/math.sqrt(float(E)),"m\nFormula:R=√(k*q/E)")
def Field_intensity_due_to_uniformly_charged_spherical_shell_on_charge__q(E,R):
	return("q=",float(E)*float(R)**2/(9*10**9),"C\nFormula:q=ER**2/k")
def Field_intensity_due_to_thin_infinite_plane_sheet_of_charge__E(sigma):
	return("E=",float(sigma)/8.854*(10**12),"V/m\nFormula:E=sigma/epsilon0")
def Field_intensity_due_to_thin_infinite_plane_sheet_of_charge_conductivity__sigma(E):
	return("sigma=",float(E)*8.854*(10**-12),"ohm**-1\nFormula:sigma=E*epsilon0")
def Current_in_a_current_carrying_conductor__I(Q,t):
	return("I=",float(Q)/float(t),"A\nFormula:I=Q/t")
def Current_in_a_current_carrying_conductor_charge__Q(I,t):
	return("Q=",float(I)*float(t),"C\nFormula:Q=I*t")
def Current_in_a_current_carrying_conductor_time__t(Q,I):
	return("t=",float(Q)/float(I),"seconds\nFormula:t=Q/I")
def Ohms_law__V(I,R):
	return("V=",float(I)*float(R),"\nFormula:V=I*R")
def Ohms_law_Current__I(V,R):
	return("I=",float(V)/float(R),"A\nFormula:I=V/R")
def Ohms_law_Resistance__R(I,V):
	return("R=",float(V)/float(I),"ohm\nFormula:R=V/I")
def Relation_between_R_and_rho__R(rho,l,A):
	return("R=",float(rho)*float(l)/float(A),"ohm\nFormula:R=rho*l/A")
def Relation_between_R_and_rho_Resistivity__Rho(R,A,l):
	return("rho=",float(R)*float(A)/float(l),"ohm metre\nFormula:rho=R*A/l")
def Relation_between_R_and_rho_Area_of_cross_section__A(rho,l,A):
	return("A=",float(rho)*float(l)/float(A),"m**2\nFormula:A=rhol/A")
def Relation_between_R_and_rho_Lenght_of_the_conductor__l(R,A,rho):
	return("l=",float(R)*float(A)/float(rho),"m\nFormula:l=RA/rho")
def Relation_between_R_and_C__C(R):
	return("C=",1/float(R),"ohm**-1\nFormula:C=1/R")
def Relation_between_R_and_C_Resistance__R(C):
	return("R=",1/float(C),"ohm\nFormula:R=1/C")
def Current_density__j(sigma,E):
	return("j=",float(sigma)*float(E),"A/m**2\nFormula:j=sigma*E")
def Current_density_conductivity__sigma(j,E):
	return("sigma=",float(j)/float(E),"\nFormula:sigma=j/E")
def Current_density_Electric_field__E(j,sigma):
	return("E=",float(j)/float(sigma),"V/m\nFormula:E=j/sigma")
def Electric_power__P(V,I):
	return("P=",float(V)*float(I),"watts\nFormula:P=V*I")
def Electric_power_Voltage__V(P,I):
	return("V=",float(P)/float(I),"\nFormula:V=P/I")
def Electric_power_Current__I(P,V):
	return("I=",float(P)/float(V),"A\nFormula:I=P/V")
def Magnetic_field_due_to_a_straight_conductor_of_infinite_length__B(N,I,r):
	return("B=",12.57*float(N)*float(I)/(float(r)*2*3.14)*(10**-7),"T\nFormula:B=µ0*N*I/2*pie*r")
def Magnetic_field_due_to_a_straight_conductor_of_infinite_length_number_of_turns__N(B,r,I):
	return("N=",float(B)*2*3.14*float(r)/(12.57*10**-7*float(I)),"\nFormula:N=B*2*pie*r/µ0*I")
def Magnetic_field_due_to_a_straight_conductor_of_infinite_length_current__I(N,B,r):
	return("I=",float(B)*2*3.14*float(r)/(12.57*10**-7*float(N)),"A\nFormula:I=B*2*pie*r/µ0*N")
def Magnetic_field_due_to_a_straight_conductor_of_infinite_length_radius__r(N,I,B):
	return("r=",(float(I)*12.57*float(N)*10**-7)/(float(B)*2*3.14),"m\nFormula:r=I*µ0*N/B*2*pie")
def Force_acting_on_a_charge_particle_in_magnetic_field__F(B,q,v,theta):
	return("F=",float(B)*float(q)*float(v)*math.sin(float(theta)),"N\nFormula:F=B*q*v*sintheta")
def Force_acting_on_a_charge_particle_in_magnetic_field_Magnetic_field__B(F,q,v,theta):
	return("B=",float(F)/(float(q)*float(v)*math.sin(float(theta))),"T\nFormula:B=F/q*v*sintheta")
def Force_acting_on_a_charge_particle_in_magnetic_field_Magnetic_field_charge__q(B,F,v,theta):
	return("q=",float(F)/(float(B)*float(v)*math.sin(float(theta))),"C\nFormula:q=F/B*v*sintheta")
def Voltage_acting_on_a_charge_particle_in_magnetic_field_velocity_of_charge_particle__v(B,q,F,theta):
	return("v=",float(F)/(float(B)*float(q)*math.sin(float(theta))),"m/s\nFormula:v=F/Bqsin(theta)")
def Force_acting_on_a_charge_particle_in_magnetic_field_angle__theta(F,B,q,v):
	return("theta=",math.asin(float(F)/float(B)*float(q)*float(v)),"degree\nFormula:theta=sin**-1(F/B*q*v)")
def Lorentz_force__F(q,E,v,B):
	return("F=",float(q)*(float(E)+(float(v)*float(B))),"N\nFormula:F=q*[E+(v*B)]")
def Lorentz_force_charge__q(F,E,v,B):
	return("q=",float(F)/(float(E)+(float(v)*float(B))),"C\nFormula:q=F/(E+(v*B))")
def Lorentz_force_Electric_field__E(F,q,v,B):
	return("E=",(float(F)/float(q))-(float(v)*float(B)),"V/m\nFormula:E=(F/q)-(v*B)")
def Lorentz_force_Velocity_of_charge_particle__v(E,F,q,B):
	return("v=",(-float(E)+(float(F)/float(q)))/float(B),"m/s\nFormula:v=(-E+(F/q))/B")
def Lorentz_force_Magnetic_field__B(E,F,q,B):
	return("B=",(-float(E)+(float(F)/float(q)))/float(B),"T\nFormula:B=(-E+(F/q))/B")
def Force_on_a_current_carrying_conductor_in_magntic_field__F(B,I,L,theta):
	return("F=",float(B)*float(I)*float(L)*math.sin(float(theta)),"N\nFormula:F=B*I*L*sintheta")
def Force_on_a_current_carrying_conductor_in_magntic_field_Magnetic_field__B(F,I,L,theta):
	return("B=",float(F)/(float(I)*float(L)*math.sin(float(theta))),"T\nFormula:B=F/(I*L*sintheta)")
def Force_on_a_current_carrying_conductor_in_magntic_field_current__I(B,F,L,theta):
	return("I=",float(F)/(float(B)*float(L)*math.sin(float(theta))),"A\nFormula:I=F/(B*L*sintheta)")
def Force_on_a_current_carrying_conductor_in_magntic_field_Lenght__L(B,I,F,theta):
	return("L=",float(F)/(float(B)*float(I)*math.sin(theta)),"m\nFormula:L=F/(B*I*sintheta)")
def Force_on_a_current_carrying_conductor_in_magntic_field_angle__theta(B,I,L,F):
	return("theta=",math.asin(float(F)/(float(B)*float(I)*float(L))),"degree\nFormula:theta=sin**-1(F/(B*I*L))")
def Torque_on_a_straight_conductor_in_magnetic_field__tau(B,I,N,A,theta):
	return("tou=",float(B)*float(I)*float(N)*float(A)*math.sin(float(theta)),"Nm\nFormula:tou=B*I*N*A*sintheta")
def Torque_on_a_straight_conductor_in_magnetic_field_magnetic_field__B(tou,I,N,A,theta):
	return("B=",float(tou)/(float(I)*float(N)*float(A)*math.sin(float(theta))),"T\nFormula:B=tou/(I*N*A*sintheta)")
def Torque_on_a_straight_conductor_in_magnetic_field_current__I(B,tou,N,A,theta):
	return("I=",float(tou)/(float(B)*float(N)*float(A)*math.sin(float(theta))),"A\nFormula:I=tou/(B*N*A*sintheta)")
def Torque_on_a_straight_conductor_in_magnetic_field_number_of_turns__N(B,I,tou,A,theta):
	return("N=",float(tou)/(float(B)*float(I)*float(A)*math.sin(float(theta))),"\nFormula:N=tou/(B*I*A*sintheta")
def Torque_on_a_straight_conductor_in_magnetic_field_Area_A(B,I,N,tou,theta):
	return("A=",float(tou)/(float(B)*float(I)*float(N)*math.sin(float(theta))),"m**2\nFormula:A=tou/(B*I*N*sintheta)")
def Torque_on_a_straight_conductor_in_magnetic_field_angle__theta(B,I,N,A,tou):
	return("theta=",math.asin(float(tou)/(float(B)*float(I)*float(N)*float(A))),"degree\nFormula:theta=sin**-1(tou/(B*I*N*A))")
def coversion_of_galvanometer_into_voltmeter__R(V,ig,G):
	return("R=",(float(V)/float(ig))-float(G),"ohm\nFormula:R=(V/ig)-G")
def coversion_of_galvanometer_into_voltmeter_voltage__V(ig,R,G):
	return("V=",float(ig)*(float(R)+float(G)),"\nFormula:V=ig*(R+G)")
def Maximum_amplitude_of_wave_interference__a(a1,a2,fi):
    A = (a1**2 + a2**2 + 2*a1*a2*cos(fi))**(1/2)
    return ('A=',A,':a=a1**2 + a2**2 + 2*a1*a2*cos(fi)')
def focus_with_given_centure_of_curvature__f(r):
	return ('f=',r/2,':f=r/2')
def focul_length_of_given_distance_between_object_and_image__f(u,v):
	return ('f=',u*v/(u+v),':f=u*v/(u+v)')
def magnifiaction_of_image_in_given_hight_of_object_and_image__m(h,H):
	return ('m=',h/H,':m=h/H')
def magnification_of_image_in_given_distance_between_object_and_image__m(u,v):
	return ('m=',u/v,':m=u/v')
def refractive_index_of_new_medium_with_respect_to_old_medium_snell_law__n(i,r):
	return ('n=',sin(i)/sin(r),':n=sin(i)/sin(r)')
def find_refractive_index_of_medium_one_to_tow_with_tow_to_one__n(n):
	return ('n=',1/n,':n=1/n')
def find_velocity_of_light_in_second_medium_with_i_r_and_v_in_first_medium__v(v,i,r):
	return ('v =', v*sin(r)/sin(i),':v = v*sin(r)/sin(i)')
def critical_angle_in_TIR__i(n):
	return ('i =', asin(n),':i = asin(n)')
def radius_of_curvature_in_given_refractive_index_of_two_medium__r(N,n,u,v):
	return ('r=',(N-n)*u*v/(u*N-v*n),':r=(N-n)*u*v/(u*N-v*n)')
def focal_length_of_lens_in_given_distance_of_oject_and_image__f(u,v):
	return ('f=',u*v/(u-v),':f=u*v/(u-v)')
def distance_of_image_through_lens_in_given_focal_length_and_distance_of_object__v(u,f):
	return ('v=',u*f/(u+f),':v=u*f/(u+f)')
def distance_of_object_through_lens_in_given_focal_length_and_distance_of_image__u(v,f):
	return ('u=',v*f/(f-v),':u=v*f/(f-v)')
def power_of_lens_in_given_focal_length__p(f):
	return ('p=',1/f,':p=1/f')
def power_of_mirror_in_given_focal_length__p(f):
	return ('p=',(-1)/f,':p=(-1)/f')
def focal_length_of_lens_in_given_power__f(p):
	return ('f=',1/p,':f=1/p')
def focal_length_of_mirror_in_given_power__f(p):
	return ('f=',1/p,':f=1/p')
def combinaction_of_two_lens__f(f,F):
	return ('f=',f*F/(f+F),':f=f*F/(f+F)')
def equivalence_magnification_of_two_lens__m(m,M):
	return ('m=',m*M,':m=m*M')
def total_deviation_of_light_in_through_prism__d(i,e,a):
	return ('d=',i+e-a,':d=i+e-a')
def refractive_index_of_prism_in_condisiton_of_light_travelling_from_medium_one_to_two__n(a,d):
	return ('n=',sin((a+d)/2)/sin(a/2),':n=sin((a+d)/2)/sin(a/2)')
def magnification_of_microscope__m(d,f):
	return ('m=',1+d/f,':m=1+d/f')
def magnification_of_compound_microscope__m(l,f):
	return ('m=',l/f,':m=l/f')
def angular_magnification_of_compound_microscope__m(d,f):
	return ('m=',1+d/f,':m=1+d/f')
def wave_length_of_light_in_medium_two_travelling_form_medium_one_to_two__L(V,v,l):
	return ('L=',V/v*l,':L=V/v*l')
def apparent_frequency_dopular_effect_in_given_velocites_of_observer_V_and_source_v__f(c,V,v,f):
	return ('f=',(c+V)/(c-v)*f,':f=(c+V)/(c-v)*f')
def distance_of_fringe_of_a_given_light__x(n,l,D,d):
	return ('x=',n*l*D/d,':x=n*l*D/d')
def resolving_power_of_lens__a(l,t):
	return ('a=',0.61*l/t,':a=0.61*l/t')
def wave_length_of_polarisation_of_light__l(k):
	return ('l=',2*pi/k,':l=2*pi/k')
def intensity_of_polarised_light_in_given_maximum_intensity_of_I__i(I,t):
	return ('i=',I(cos(t))**2,':i=I(cos(t))**2')
def kinetic_energy_of_electron_in_a_incident_of_light__k(v):
	return ('k=',1.9*10**(-19)*v,':k=1.9*10**(-19)*v')
def wave_length_of_partcle__l(m,v):
	return ('l=',6.626*10**(-34)/(m*v),':l=6.626*10**(-34)/(m*v)')
def deBroglie_wave_lenght__l(v):
	return ('l=',1.227/v**0.5,':l=1.227/v**0.5')
def total_energy_of_electron__e(r):
	return ('e=',((-1)*1.9*10**(-19))**2/(8*pi*(8.854187817*10**(-12))*r),':e=((-1)*1.9*10**(-19))**2/(8*pi*(8.854187817*10**(-12))*r)')
def frequency_of_light_emighted_when_electron_travel_form_starting_N_to_ending_n_orbit__f(n,N):
	return ('f=',(1.097*10**7)*(1/n**2-1/N**2),':f=(1.097*10**7)*(1/n**2-1/N**2)')
def velocity_of_electron_in_nth_orbit__v(n):
	return ('v=',(1.9*10**(-19))**2/(n*2*8.854187817*10**(-12)*1.097*10**7),':v=(1.9*10**(-19))**2/(n*2*8.854187817*10**(-12)*1.097*10**7)')
def radius_of_orbit_at_nth_orbit__r(n):
	return ('r=',n**2*(1.097*10**7)**2*8.854187817*10**(-12)/(pi*(9.1093837*10**(-31))*(1.9*10**(-19))**2),':r=n**2*(1.097*10**7)**2*8.854187817*10**(-12)/(pi*(9.1093837*10**(-31))*(1.9*10**(-19))**2)')
def total_energy_of_electron_orbiting_at_nth_orbit__e(n):
	return ('e=',-2.18*10*(-19)/n**2,':e=-2.18*10*(-19)/n**2')
def energy_of_nuclear_binding_energy__e(m):
	return ('e=',m*(3*10**8)**2,':e=m*(3*10**8)**2')
def radioactivity_active_decay_at_given_time_t__n(N,l,t):
	return ('n=',N*e**(-l*t),':n=N*e**(-l*t)')
