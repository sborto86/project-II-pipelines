### PLOTTING FUNCTIONS

def country_plot(df, country, platform, fl=8, fh=6, mx=0.1, my=0.05, names="all"):
    '''
    Function to plot the number of hotels for each city in a Geopandas countru map
        df: DataFrame, with columns agoda_num and booking_num
        country: string, name in english of a Country
        platform: string, name of the platform "agoda" or "booking"
        fl: int, figure lenght
        fh: figure height
        mx: margins in x axis
        my: margin in y axis
        names: str ("all", "top", "none") add labels with the names of the cities ploted in the map 
    '''
    if "plt" not in dir():
        import matplotlib.pyplot as plt
    if "gpd" not in dir():
        import geopandas as gpd
    vmaxi = df.agoda_num.max()*1.1
    if platform == "agoda":
        coln = "agoda_num"
        color = "Reds"
    elif platform == "booking":
        coln = "booking_num"
        color = "Blues"
    else:
        print("Platform not avaliable")
        pass
    # initialize axis
    fig, ax = plt.subplots(figsize=(fl,fh))
    # plot map on axis
    countries = gpd.read_file(  
         gpd.datasets.get_path("naturalearth_lowres"))
    countries[countries["name"] == country].plot(color="lightgrey", ax=ax)
    # plot points
    df.plot(x="longitude", y="latitude", kind="scatter", 
            c=coln, s=df[coln]/2, colormap=color, vmax=vmaxi, vmin=0, alpha=0.7,
            title=f"Hotels {country} in {platform.capitalize()}", 
            ax=ax)
    # adding names of the cities
    if names == "all":
        for i in range(df.shape[0]):
            plt.text(x=df.longitude[i]+0.01, y=df.latitude[i]-0.03,s=df.city[i], fontdict=dict(size=8))
    elif names == None:
        pass
    elif names == "top":
        top = df.agoda_num.max()/5
        for i in range(df.shape[0]):
            if df.agoda_num[i] > top:
                plt.text(x=df.longitude[i]+0.01, y=df.latitude[i]-0.03,s=df.city[i], fontdict=dict(size=8))
    #Removing X and Y labels
    plt.xlabel("")
    plt.ylabel("")
    #adding padding
    plt.margins(0.1, 0.05)
    ax.collections[-1].colorbar.set_label("Number of Hotels")
    # adding grid
    ax.grid(visible=True, alpha=0.5)
    return fig

def country_comp (df, country, fl=16, fh=8, mx=0.1, my=0.05, names="all"):
    '''
    Function to plot a comparison figure between agoda and booking with the number of hotels in a country
        df: DataFrame, with columns agoda_num and booking_num
        country: string, name in english of a Country
        fl: int, figure lenght
        fh: figure height
        mx: margins in x axis
        my: margin in y axis
        names: str ("all", "top", "none") add labels with the names of the cities ploted in the map 
    '''
    if "plt" not in dir():
        import matplotlib.pyplot as plt
    if "gpd" not in dir():
        import geopandas as gpd
    ## Setting max number of hotels
    if df.agoda_num.max() >= df.booking_num.max():
        vmaxi = df.agoda_num.max()*1.1
    else:
        vmaxi = df.booking_num.max()*1.1
    # initialize axis
    fig, axs = plt.subplots(1, 2, figsize=(fl,fh), gridspec_kw={"width_ratios":[1,1]})
    # plot map on axis
    countries = gpd.read_file(  
        gpd.datasets.get_path("naturalearth_lowres"))
    countries[countries["name"] == country].plot(color="lightgrey", ax=axs[0])
    # plot points
    df.plot(x="longitude", y="latitude", kind="scatter", 
    c="agoda_num", s=df["agoda_num"]/2, colormap="Wistia", vmax=df.agoda_num.max()*1.1, vmin=0, alpha=0.7,
    title=f"Hotels  {country} in Agoda", 
    ax=axs[0])
    # adding names of the cities
    if df.agoda_num.max() >= df.booking_num.max():
        top = df.agoda_num.max()/5
        for i in range(df.shape[0]):
            if df.agoda_num[i] > top:
                axs[0].text(x=df.longitude[i]+0.01, y=df.latitude[i]-0.03,s=df.city[i], fontdict=dict(size=8))
                axs[1].text(x=df.longitude[i]+0.01, y=df.latitude[i]-0.03,s=df.city[i], fontdict=dict(size=8))
    else:
        top = df.booking_num.max()/5
        for i in range(df.shape[0]):
            if df.booking_num[i] > top:
                axs[0].text(x=df.longitude[i]+0.01, y=df.latitude[i]-0.03,s=df.city[i], fontdict=dict(size=8))
                axs[1].text(x=df.longitude[i]+0.01, y=df.latitude[i]-0.03,s=df.city[i], fontdict=dict(size=8))
    #Removing X and Y labels
    axs[0].set(xlabel='', ylabel='')
    #adding padding
    plt.margins(0.1, 0.05)
    axs[0].collections[-1].colorbar.set_label("Number of Hotels")
    # adding grid
    axs[0].grid(visible=True, alpha=0.5)
    countries = gpd.read_file(  
        gpd.datasets.get_path("naturalearth_lowres"))
    countries[countries["name"] == country].plot(color="lightgrey", ax=axs[1])
    df.plot(x="longitude", y="latitude", kind="scatter", 
        c="booking_num", s=df["booking_num"]/2, colormap="cool", vmax=df.agoda_num.max()*1.1, vmin=0, alpha=0.7,
    title=f"Hotels {country} in Booking", 
    ax=axs[1])
    axs[1].grid(visible=True, alpha=0.5)
    axs[1].collections[1].colorbar.set_label("Number of Hotels")
    axs[1].set(xlabel='', ylabel='')
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.tight_layout()
    return fig