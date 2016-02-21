import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import GPy

class Video(object):
    """An object to hold all the data of a video we are analyzing."""
    
    def __init__(self, video_info, ratings):
        """Initialize Video object.
        
        :param video_info: list containing [genre, video_id, title, url, duration]
        :param ratings: list of lists containing ratings
        """
        
        self.genre = video_info[0]
        self.id = video_info[1]
        self.title = video_info[2]
        self.url = video_info[3]
        minutes, seconds = [int(v) for v in video_info[4].split(":")]
        self.duration = minutes * 60 + seconds

        # Get a list of ratings
        self.ratings = ratings
        self.samples = []
        
        # Get samples
        self._sample_ratings()
        self.sample_locations = self._get_sample_locations()
        self.sample_data = self._get_flattened_samples()
        
        # Gaussian Process Information
        self.kernel = None
        self.gp = None
        
        # Kernel Params
        self.kernel_variance = 2.29
        self.lengthscale = 60.0
        
        
    def _sample_ratings(self):
        """Get rating from every 2 seconds.
        
        Original video has 60 of every value (60 frames @ 30 fps).
        """
        # Get a sample from every 2 seconds.
        for rating in self.ratings:
            sample = []
            for i, score in enumerate(rating):
                if i % 60 == 0:
                    sample.append(int(score))
            self.samples.append(sample)
        
    def plot_samples(self, n_boot=500):
        """Plot our samples using Seaborn tsplot and Bootstrap sampling.
        
        :param n_boot: Number of Bootstrap sampling iterations
        """
        
        plt.figure(figsize=(16, 12))
        sns.tsplot(self.samples, err_style="boot_traces", n_boot=n_boot)
        plt.title("Ratings with Bootstrap resampling")
        plt.xlabel("Time (every 2 seconds)")
        plt.ylabel("Rating")
        
    def _get_sample_locations(self):
        """Rescale sample locations to be every 60 frames."""
        
        locations = range(len(self.samples[0]))
        sample_locs = [x * 60 for x in locations]
        
        # Create 20x sample_locations for our 20 annotators
        return np.reshape(np.array(sample_locs * 20), (-1, 1))
    
    def _get_flattened_samples(self):
        """Flatten the samples into one Nx1 np array"""
        
        flattened_list = [item for sublist in self.samples for item in sublist]
        return np.reshape(np.array(flattened_list), (-1, 1))
    
    def X(self):
        """Return Sample Locations (X in a model)"""
        
        return self.sample_locations
    
    def Y(self):
        """Return Sample Data (Y in a model)"""
        
        return self.sample_data
    
    def fit_gaussian_process(self, variance=2.29, lengthscale=60.0, 
                             print_gp = True, optimize=False):
        """Fit a Gaussian Process with an RBF Kernel for our rating data.
        
        :param variance: float - The Variance of the RBF Kernel
        :param lengthscale: float - The lengthscale of the RBF Kernel
        :param print_gp: bool (Default=True) - Prints GP information
        :param optimize: bool (Default=False) - Optimizes GP to minimize
                                                loglikelyhood by modifying
                                                Variance and Lengthscale of
                                                kernel.
        
        """
        kernel = GPy.kern.RBF(input_dim=1, variance=variance, lengthscale=lengthscale)
        self.gp = GPy.models.GPRegression(self.sample_locations, self.sample_data, kernel)
        
        if optimize:
            self.gp.optimize(messages=False)
        if print_gp:
            print self.gp
        
    def plot_gaussian_process(self):
        """Plots Gaussian Process."""
        if not self.gp:
            print "Please call fit_gaussian_process first."
            return
        fig = gp.plot()
