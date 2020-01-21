#!/usr/bin/env python
import ROOT, sys
from ROOT import std
from larcv import larcv
from numpy import array

if len(sys.argv) < 2:

   print('Usage: python',sys.argv[0],'CONFIG_FILE [LARCV_FILE1 LARCV_FILE2 ...]')
   sys.exit(1)

proc = larcv.ProcessDriver('ProcessDriver')

proc.configure(sys.argv[1])

if len(sys.argv) > 1:
   
   flist=ROOT.std.vector('std::string')()
   for x in range(len(sys.argv)-2):
      flist.push_back(sys.argv[x+2])
      
   proc.override_input_file(flist)
   
reco_id = proc.process_id("LArbysImage")
ana_id  = proc.process_id("LArbysImageAna")

larbysimg     = proc.process_ptr(reco_id)
larbysimg_ana = proc.process_ptr(ana_id)
larbysimg_ana.SetManager(larbysimg.Manager())

proc.override_ana_file("colinear_yplane.root")

proc.initialize()

#(>= 0.98 or <= -0.98)
events=array([ 1023,  1233,  1424,  1679,  1935,  3201,  3576,  4159,  4172,
                4222,  4349,  4550,  5025,  6010,  6101,  6360,  6390,  6797,
                6879,  7130,  7318,  7404,  8004,  8167,  8578,  8603,  8718,
                9172,  9307,  9482,  9554, 10151, 10795, 10823, 11084, 11295,
               11304, 11599, 11856, 12137, 12419, 13027, 13494, 13703, 13784,
               13904, 14016, 14778, 15036, 15296, 15419, 15529, 15607, 15979,
               16106, 16154, 16521, 16836, 17066, 17109, 17274, 17290, 17350,
               18730, 18871, 19147, 19166, 19965, 20488, 20824, 20946, 22175,
               22835, 22879, 23602,   329,   463,   575,  1340,  1479,  1504,
                1729,  1973,  2145,  2167,  2332,  2644,  2997,  3266,  3358,
                3550,  3653,  3719,  3879,  3892,  3971,  4062,  4141,  4217,
                4377,  4578,  4581,  4602,  4624,  4652,  4666,  4737,  4885,
                5127,  5292,  5435,  5476,  5598,  5803,  5907,  6155,  6294,
                6348,  6403,  6448,  6777,  6817,  6822,  6921,  7018,  7098,
                7234,  7300,  7415,  7453,  7674,  7923,  7966,  8060,  8397,
                8927,  9153,  9222,  9252,  9285, 10017, 10078, 10119, 10157,
               10269, 10292, 11128, 11198, 11562, 11583, 11649, 11650, 11652,
               11734, 11891, 12021, 12025, 12029, 12442, 12662, 12724, 13289,
               13768, 13821, 13883, 13918, 14022, 14125, 14387, 14537, 14622,
               14624, 14650, 15143, 15299, 15484, 15553, 15568, 15832, 15880,
               16253, 16509, 16828, 16978, 17664, 18007, 18083, 18516, 18557,
               18703, 19430, 19541, 20056, 20156, 20186, 20470, 20646, 20648,
               20658, 20676, 20811, 20884, 21324, 21524, 21580, 22036, 22070,
               22093, 22162, 22329, 22363, 22463, 22512, 22576, 22645, 22702,
               22771, 23629, 23649, 23835, 24830])

# events=array([  373,   709,   726,   835,   847,   895,  1027,  1263,  1295,
#                 1312,  1343,  1401,  1450,  1491,  1562,  1605,  1716,  1777,
#                 2051,  2135,  2440,  2442,  2467,  2821,  2897,  2973,  3119,
#                 3221,  3323,  3411,  3473,  3544,  3634,  3737,  3781,  3785,
#                 3871,  3982,  3986,  4058,  4235,  4309,  4384,  4406,  4452,
#                 4587,  4665,  4883,  5065,  5100,  5154,  5275,  5489,  5735,
#                 5779,  5833,  6045,  6206,  6375,  6467,  6981,  7028,  7350,
#                 7417,  7546,  7768,  7938,  8025,  8388,  8475,  8535,  8565,
#                 8655,  8715,  8763,  8908,  8916,  9001,  9053,  9066,  9260,
#                 9438,  9593,  9605,  9610,  9663,  9869, 10225, 10375, 10487,
#                 10514, 10640, 10730, 10955, 11059, 11144, 11371, 11543, 11708,
#                 11844, 11937, 12113, 12181, 12489, 12529, 12703, 12821, 12870,
#                 12887, 12992, 13095, 13098, 13141, 13398, 13622, 13734, 13915,
#                 14031, 14400, 14653, 14949, 15001, 15091, 15427, 15521, 15654,
#                 15867, 16043, 16153, 16581, 16702, 17004, 17029, 17232, 17346,
#                 17366, 17703, 17735, 17811, 18038, 18325, 18330, 18372, 18492,
#                 18571, 18642, 18917, 18949, 19004, 19009, 19356, 19373, 19581,
#                 19692, 19802, 19818, 20025, 20064, 20334, 20383, 20510, 20765,
#                 20771, 20793, 21063, 21176, 21230, 21555, 21828, 21839, 22071,
#                 22094, 22187, 22424, 22465, 22711, 22794, 23007, 23083, 23188,
#                 23217, 23302, 23341, 23442, 23514, 23584, 23596, 23657, 23711,
#                 24758, 26890])
step=1
for evstart in events:
   print("On event: ",evstart)
   proc.batch_process(evstart,step)

proc.finalize()
