Vim�UnDo� "�X�2��yr6�SqE��(�Bw�b�jLG�   M   8fir,=np.load("4_clase/low_pass_short.npy").astype(float)                             ^�z�    _�                             ����                                                                                                                                                                                                                                                                                                                                                          ^�e�     �          M      (xLn,  = plt.plot(tData[0:N],xData,'g-o')   xAxe.grid(True)   hAxe  = fig.add_subplot(1,2,2)   &hLn,  = plt.plot(tData[0:M],fir,'r-o')   hAxe.grid(True)�         M      xAxe  = fig.add_subplot(1,2,1)5�_�                    !        ����                                                                                                                                                                                                                                                                                                                            !           L                   ^�e�    �       M   M   ,   #for i in range(N):   '#    xAxe  = fig.add_subplot(6,3,3*i+1)   K#    xLn,xHighLn,  = plt.plot(tData[0:N],xData,'r-',tData[i],xData[i],'yo')   #    xLnArray.append(xLn)   #    xAxe.grid(True)   #    xAxe.set_xlim(0,N-1)   7#    xAxe.set_ylim(np.min(xData)-0.2,np.max(xData)+0.2)   (##--------------------------------------   
#hData=fir   #yData=np.zeros(N+M-1)   #hLn=[]   #yLn=[]   #for i in range(N):   '#    hAxe  = fig.add_subplot(6,3,3*i+2)   !#    Ln,  = plt.plot([],[],'b-o')   8#    #Ln,  = plt.plot(tData[i:M+i],hData*xData[i],'r-o')   #    hLn.append(Ln)   #    hAxe.grid(True)   #    hAxe.set_xlim(0,N+M-2)   I#    hAxe.set_ylim(np.min(hData*xData[i])-0.1,np.max(hData*xData[i])+0.1)   (##--------------------------------------   '#    yAxe  = fig.add_subplot(6,3,3*i+3)   !#    yData[i:i+M]+=hData*xData[i]   !#    Ln,  = plt.plot([],[],'b-o')   1#    #Ln,  = plt.plot(tData[0:N+M-1],yData,'b-o')   #    yLn.append(Ln)   #    yAxe.grid(True)   #    yAxe.set_xlim(0,N+M-2)   9#    yAxe.set_ylim(np.min(yData)-0.01,np.max(yData)+0.01)   (##--------------------------------------   #yData=np.zeros(N+M-1)   #def init():   #    return yLn,hLn   #   #def update(i):   1#    hLn[i].set_data(tData[i:M+i],hData*xData[i])   !#    yData[i:i+M]+=hData*xData[i]   *#    yLn[i].set_data(tData[0:N+M-1],yData)   #    ani.event_source.stop()   #    return yLn,hLn   #   J#ani=FuncAnimation(fig,update,N,init,interval=50 ,blit=False,repeat=False)   5#plt.get_current_fig_manager().window.showMaximized()   #b=buttonOnFigure(fig,ani)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       ^�z�    �   
      M      8fir,=np.load("4_clase/low_pass_short.npy").astype(float)5��