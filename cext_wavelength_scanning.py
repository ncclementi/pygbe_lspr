


def Cext_analytical(radius, wavelength, diel_in, diel_out):
    '''Calculates the analytical solution of the extinction cross section.
       This solution is valid when the nano particle involved is a sphere. 
    
    Arguments:
    ----------
    radius    : float, radius of the sphere in [nm].
    wavelength: float, wavelength of the incident electric field in [nm].
    diel_in   : complex, dielectric constant inside surface. 
    diel_out  : complex, dielectric constant inside surface.

    Returns:
    --------
    Cext_an   : float, extinction cross section.
      
    '''
    wavenumber = 2*numpy.pi*numpy.sqrt(diel_out)/wavelength
    C1 = wavenumber**2*(diel_in/diel_out-1)/(diel_in/diel_out+2)
    Cext_an = 4*numpy.pi*radius**3/wavenumber.real * C1.imag 
    
    return Cext_an
