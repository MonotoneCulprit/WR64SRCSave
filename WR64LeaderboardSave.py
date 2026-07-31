#!/usr/bin/env python3
# Creating a Wave Race 64 Save using the current top 3 times for each track.

import os
import sys
import srcomapi
import srcomapi.datatypes as dt
import requests
import json
import pandas as pd
import ids
import splits
import savemanipulation as sm

api = srcomapi.SpeedrunCom()

# Get 3 Lap top 3 data for each level
SB3data = sm.gettopthree(ids.SB_id, ids.ThreeL_id)
SBay3data = sm.gettopthree(ids.SBay_id, ids.ThreeL_id)
DL3data = sm.gettopthree(ids.DL_id, ids.ThreeL_id)
MF3data = sm.gettopthree(ids.MF_id, ids.ThreeL_id)
PB3data = sm.gettopthree(ids.PB_id, ids.ThreeL_id)
TC3data = sm.gettopthree(ids.TC_id, ids.ThreeL_id)
GC3data = sm.gettopthree(ids.GC_id, ids.ThreeL_id)
SI3data = sm.gettopthree(ids.SI_id, ids.ThreeL_id)

# Get 1 Lap World Record data for each level
SB1data = sm.gettoprun(ids.SB_id)
SBay1data = sm.gettoprun(ids.SBay_id)
DL1data = sm.gettoprun(ids.DL_id)
MF1data = sm.gettoprun(ids.MF_id)
PB1data = sm.gettoprun(ids.PB_id)
TC1data = sm.gettoprun(ids.TC_id)
GC1data = sm.gettoprun(ids.GC_id)
SI1data = sm.gettoprun(ids.SI_id)

# Get Reverse World Record data for each level
SBRdata = sm.gettopthree(ids.SB_id, ids.Reverse_id)
SBayRdata = sm.gettopthree(ids.SBay_id, ids.Reverse_id)
DLRdata = sm.gettopthree(ids.DL_id, ids.Reverse_id)
MFRdata = sm.gettopthree(ids.MF_id, ids.Reverse_id)
PBRdata = sm.gettopthree(ids.PB_id, ids.Reverse_id)
TCRdata = sm.gettopthree(ids.TC_id, ids.Reverse_id)
GCRdata = sm.gettopthree(ids.GC_id, ids.Reverse_id)
SIRdata = sm.gettopthree(ids.SI_id, ids.Reverse_id)

# Isolate 3 Lap times and names into individual variables for each level
SB3firsttime, SB3secondtime, SB3thirdtime = sm.extracttimes_mariner(SB3data)
SB3firstname, SB3secondname, SB3thirdname = sm.extractnames(SB3data)
SBay3firsttime, SBay3secondtime, SBay3thirdtime = sm.extracttimes_mariner(SBay3data)
SBay3firstname, SBay3secondname, SBay3thirdname = sm.extractnames(SBay3data)
DL3firsttime, DL3secondtime, DL3thirdtime = sm.extracttimes_mariner(DL3data)
DL3firstname, DL3secondname, DL3thirdname = sm.extractnames(DL3data)
MF3firsttime, MF3secondtime, MF3thirdtime = sm.extracttimes_jeter(MF3data)
MF3firstname, MF3secondname, MF3thirdname = sm.extractnames(MF3data)
PB3firsttime, PB3secondtime, PB3thirdtime = sm.extracttimes_jeter(PB3data)
PB3firstname, PB3secondname, PB3thirdname = sm.extractnames(PB3data)
TC3firsttime, TC3secondtime, TC3thirdtime = sm.extracttimes_mariner(TC3data)
TC3firstname, TC3secondname, TC3thirdname = sm.extractnames(TC3data)
GC3firsttime, GC3secondtime, GC3thirdtime = sm.extracttimes_mariner(GC3data)
GC3firstname, GC3secondname, GC3thirdname = sm.extractnames(GC3data)
SI3firsttime, SI3secondtime, SI3thirdtime = sm.extracttimes_mariner(SI3data)
SI3firstname, SI3secondname, SI3thirdname = sm.extractnames(SI3data)

# Isolate 1 Lap times and names into individual variables for each level
SB1time = sm.extracttime_mariner(SB1data)
SB1name = SB1data.Player[0]
SBay1time = sm.extracttime_mariner(SBay1data)
SBay1name = SBay1data.Player[0]
DL1time = sm.extracttime_mariner(DL1data)
DL1name = DL1data.Player[0]
MF1time = sm.extracttime_jeter(MF1data)
MF1name = MF1data.Player[0]
PB1time = sm.extracttime_jeter(PB1data)
PB1name = PB1data.Player[0]
TC1time = sm.extracttime_mariner(TC1data)
TC1name = TC1data.Player[0]
GC1time = sm.extracttime_mariner(GC1data)
GC1name = GC1data.Player[0]
SI1time = sm.extracttime_mariner(SI1data)
SI1name = SI1data.Player[0]

# Isolate Reverse time and name into individual variables for each level
SBRtime = sm.extracttime_mariner(SBRdata)
SBRname = SBRdata.Player[0]
SBayRtime = sm.extracttime_mariner(SBayRdata)
SBayRname = SBayRdata.Player[0]
DLRtime = sm.extracttime_mariner(DLRdata)
DLRname = DLRdata.Player[0]
MFRtime = sm.extracttime_hayami(MFRdata)
MFRname = MFRdata.Player[0]
PBRtime = sm.extracttime_jeter(PBRdata)
PBRname = PBRdata.Player[0]
TCRtime = sm.extracttime_mariner(TCRdata)
TCRname = TCRdata.Player[0]
GCRtime = sm.extracttime_mariner(GCRdata)
GCRname = GCRdata.Player[0]
SIRtime = sm.extracttime_mariner(SIRdata)
SIRname = SIRdata.Player[0]

# Start building the save file

# Write Header
sm.writetooffset(bytes.fromhex('5445'), 0x0)

# Write FF Spaces
sm.writetooffset(bytes.fromhex('FFFFFFFF'), 0x4)

# Unlock all tracks and difficulties
sm.writetooffset(bytes.fromhex('06060707'), 0x8)

# Unlock all Championships and set Audio to Stereo with Music On
sm.writetooffset(bytes.fromhex('0F'), 0xC)

# Write FF Spaces
sm.writetooffset(bytes.fromhex('FFFFFF'), 0xD)
