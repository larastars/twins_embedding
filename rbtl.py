import numpy as np
import extinction

def negative_log_likelihood(params, max_flux, fluxerr, color_law, mean_flux, intrinsic_dispersion):
	"""
	 To implement:
	from scipy import minimize
	self.fractional_dispersion = np.std(self.maximum_flux, axis = 0) / np.mean(self.maximum_flux, axis=0)
	mean_flux = np.mean(self.maximum_flux, axis=0)
	for i in range(len(self.maximum_flux)):
	    opt = minimize(negative_log_likelihood, 
	            [0., 0.], 
	            args = (self.maximum_flux[i],
	                self.maximum_fluxerr[i],
	                self.rbtl_color_law,
	                mean_flux,
	                self.fractional_dispersion)
	            )
	    print(self.targets[i])
	    print(opt.x)

    """
	dm, color = params
	scale = 10**(0.4 * (dm + color * color_law))
	scale_flux = max_flux * scale
	scale_fluxerr = fluxerr * scale
	sigma_sq = (intrinsic_dispersion * mean_flux)**2 + scale_fluxerr**2

	return np.sum(0.5 * (scale_flux - mean_flux)**2 / (sigma_sq) + np.log(np.sqrt(sigma_sq)))


def negative_log_likelihood_multiple(params, max_flux, fluxerr, color_law):
	"""
	Parameters
	----------
		params: 
			unpacks to dm, color.  dm is shape [N_SNe], color is [N_SNe]
		max_flux:
			all max flux spectra, shape is [N_SNe, N_bins]
		fluxerr:
			corresponds to max flux
		color_law:
			fitzpatrick dust law



	To implement this:
	opt = minimize(negative_log_likelihood_multiple,
				np.zeros([2*len(self.maximum_flux)]),
				args = (self.maximum_flux,
						self.maximum_fluxerr,
						self.rbtl_color_law))
	print(opt.x)
	"""
	dm, color = params[:len(max_flux)], params[len(max_flux):]
	color_law = np.array(color_law).reshape(1, len(color_law))
	color_law = np.repeat(color_law, len(max_flux), axis = 1)
	scale = 10**(0.4 * (dm + color * color_law))
	scale_flux = max_flux * scale
	scale_fluxerr = fluxerr * scale
	mean_flux = np.mean(scale_flux, axis=0)
	intrinsic_dispersion = np.std(scale_flux, axis=0) / mean_flux
	sigma_sq = (intrinsic_dispersion * mean_flux)**2 + scale_fluxerr**2

	return np.sum(0.5 * (scale_flux - mean_flux)**2 / (sigma_sq) + np.log(np.sqrt(sigma_sq)))