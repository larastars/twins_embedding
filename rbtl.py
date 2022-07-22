import numpy as np
import extinction

def negative_log_likelihood(params, max_flux, fluxerr, color_law, mean_flux, intrinsic_dispersion):
	dm, color = params
	scale = 10**(0.4 * (dm + color * color_law))
	scale_flux = max_flux * scale
	scale_fluxerr = fluxerr * scale
	sigma_sq = (intrinsic_dispersion * mean_flux)**2 + scale_fluxerr**2

	return np.sum(0.5 * (scale_flux - mean_flux)**2 / (sigma_sq) + np.log(np.sqrt(sigma_sq)))

# To implement:
# from scipy import minimize
# self.fractional_dispersion = np.std(self.maximum_flux, axis = 0) / np.mean(self.maximum_flux, axis=0)
# mean_flux = np.mean(self.maximum_flux, axis=0)
# for i in range(len(self.maximum_flux)):
#     opt = minimize(negative_log_likelihood, 
#             [0., 0.], 
#             args = (self.maximum_flux[i],
#                 self.maximum_fluxerr[i],
#                 self.rbtl_color_law,
#                 mean_flux,
#                 self.fractional_dispersion)
#             )
#     print(self.targets[i])
#     print(opt.x)