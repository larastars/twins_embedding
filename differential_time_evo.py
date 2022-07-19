def diff_time_evo(phase):
    diff = phase*c1 + (phase**2)*c2
    return diff

def spec_from_peak(peak_spec, phase):
    diff = diff_time_evo(phase)
    return peak_spec + diff

sigma_gray = 0.02
def mag_2_flux(mag_spec, m_gray):
    return 10**(-0.4*mag_spec + m_gray)

def neg_log_posterior(params, flux_obs, fluxerr_obs, c1, c2, phases):
    """
    Parameters
    ----------
    params: np array
        Last element should be the magnitude of gray offset, all other elements are the peak spectrum being predicted
    flux_obs: np.array
        Spectra within 5 days of peak.  Shape: [N_spectra x N_bins]
    fluxerr_obs:
        Uncertainties of near-peak spectra.  Same shape as flux_obs
    c1:
        Phase slope coefficients.  Shape [N_bins]
    c2:
        Phase quadratic coefficients.  Shape [N_bins]
    phases:
        List of near-peak spectra phases.  If single phase should still be cast as list. Shape [N_spectra]
        
    
    Returns
    -------
    Negative log posterior of data given model (model is simply peak spectrum and gray offset)
    
    Note: I'm not yet sure how to enfore variance of grey offset! Let's see how it turns out...?
    
    """
    peak_spec = params[:-1]
    m_gray = params[-1]
    running_log_posterior = 0
    for phase in phases:
        pred_spec = spec_from_peak(peak_spec, phase)
        pred_flux_spec = mag_2_flux(pred_spec, m_gray) # how to include variance of m_gray??
        sigma_sq = fluxerr_obs**2 + epsilon(phase)*pred_flux_spec
        log_posterior = -0.5*(pred_flux_spec - flux_obs)**2 / (sigma_sq)
        running_log_posterior += log_posterior
        
    return -1 * running_log_posterior

def diff_time_evo(phase):
    diff = phase*c1 + (phase**2)*c2
    return diff

def spec_from_peak(peak_spec, phase):
    diff = diff_time_evo(phase)
    return peak_spec + diff

sigma_gray = 0.02
def mag_2_flux(mag_spec, m_gray):
    return 10**(-0.4*mag_spec + m_gray)

def neg_log_posterior(params, flux_obs, fluxerr_obs, c1, c2, phases):
    """
    Parameters
    ----------
    params: np array
        Last element should be the magnitude of gray offset, all other elements are the peak spectrum being predicted
    flux_obs: np.array
        Spectra within 5 days of peak.  Shape: [N_spectra x N_bins]
    fluxerr_obs:
        Uncertainties of near-peak spectra.  Same shape as flux_obs
    c1:
        Phase slope coefficients.  Shape [N_bins]
    c2:
        Phase quadratic coefficients.  Shape [N_bins]
    phases:
        List of near-peak spectra phases.  If single phase should still be cast as list. Shape [N_spectra]
        
    
    Returns
    -------
    Negative log posterior of data given model (model is simply peak spectrum and gray offset)
    
    Note: I'm not yet sure how to enfore variance of grey offset! Let's see how it turns out...?
    
    """
    peak_spec = params[:-1]
    m_gray = params[-1]
    running_log_posterior = 0
    for phase in phases:
        pred_spec = spec_from_peak(peak_spec, phase)
        pred_flux_spec = mag_2_flux(pred_spec, m_gray) # how to include variance of m_gray??
        sigma_sq = fluxerr_obs**2 + epsilon(phase)*pred_flux_spec
        log_posterior = -0.5*(pred_flux_spec - flux_obs)**2 / (sigma_sq)
        running_log_posterior += log_posterior
        
    return -1 * running_log_posterior

# To implement do something like:

from scipy import minimize
c1 = #get phase_slope from stan model cache
c2 = #get phase_quadratic from stan model cache
for i in range(num_targets):
    peak_spectra = self.flux[...] #find near-peak spectra for this SN
    peak_errs = self.fluxerr[] #do same thing!
    peak_phases = ... #phases of near-peak spectra
    opt = minimize(neg_log_posterior, 
            np.zeros(288 + 1), 
            args = (peak_spectra,
                peak_errs,
                c1,
                c2,
                peak_phases)
            )
    print(self.targets[i])
    print(opt.x)