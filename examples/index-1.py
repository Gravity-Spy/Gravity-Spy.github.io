from gwpy.table import EventTable
from gwpy.segments import DataQualityFlag
aftercommissionseg_l1 = DataQualityFlag.query('H1:DMT-ANALYSIS_READY:1',1178841618, 1186963218)
beforecommissionseg_l1 = DataQualityFlag.query('H1:DMT-ANALYSIS_READY:1', '2016-11-30', 1178841618)
blips_O2 = EventTable.fetch('gravityspy','glitches',selection='"Label "="Blip" & "peakGPS" > 1137250000 & "Blip" > 0.95')
koi_O2 = EventTable.fetch('gravityspy','glitches',selection='"Label "="Koi_Fish" & "peakGPS" > 1137250000 & "Koi_Fish" > 0.95')
aftercomiss_koi_l1 = koi_O2[(koi_O2['peakGPS']>1178841618) & (koi_O2['ifo']=='L1')]
beforecomiss_koi_l1 = koi_O2[(koi_O2['peakGPS']<1178841618) & (koi_O2['ifo']=='L1')]
beforecomiss_blips_l1 = blips_O2[(blips_O2['peakGPS']<1178841618) & (blips_O2['ifo']=='L1')]
aftercomiss_blips_l1 = blips_O2[(blips_O2['peakGPS']>1178841618) & (blips_O2['ifo']=='L1')]
plot = aftercomiss_blips_l1.hist('snr', logbins=True, bins=50, histtype='stepfilled', label='After Commissioning')
ax = plot.gca()
ax.hist(aftercomiss_koi_l1['snr'], logbins=True, bins=50, histtype='stepfilled', label='After Commissioning Koi')
ax.hist(beforecomiss_blips_l1['snr'], weights=float(abs(aftercommissionseg_l1.active)/abs(beforecommissionseg_l1.active)), logbins=True, bins=50, histtype='stepfilled', label='Before Commissioning')
ax.hist(beforecomiss_koi_l1['snr'], weights=float(abs(aftercommissionseg_l1.active)/abs(beforecommissionseg_l1.active)), logbins=True, bins=50, histtype='stepfilled', label='Before Commissioning Koi')
ax.set_xlabel('Signal-to-noise ratio (SNR)')
ax.set_ylabel('Rate')
ax.set_title('Blips and Kois before and after comissioning L1')
ax.autoscale(axis='x', tight=True)
ax.set_xlim([0,1000])
plot.add_legend()
plot.show()
