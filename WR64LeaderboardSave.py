#!/usr/bin/env python3
# Creating a Wave Race 64 Save using the current top 3 times for each track.

import os
import sys
from datetime import datetime
import srcomapi
import srcomapi.datatypes as dt
import requests
import json
import pandas as pd
import ids
import splits
import savemanipulation as sm

# Connect to srcomapi
api = srcomapi.SpeedrunCom()

# Create blank save with today's date
now = datetime.now()
date_string = now.strftime("%m-%d-%Y")
filename = f"wr64_srcomsave_{date_string}.eep"
with open("Output/" + filename, "wb") as file:
    file.write((b"\x00") * (0x1FF + 1))

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
SB3firstname = sm.createinitialshex(SB3firstname)
SB3secondname = sm.createinitialshex(SB3secondname)
SB3thirdname = sm.createinitialshex(SB3thirdname)
SBay3firsttime, SBay3secondtime, SBay3thirdtime = sm.extracttimes_mariner(SBay3data)
SBay3firstname, SBay3secondname, SBay3thirdname = sm.extractnames(SBay3data)
SBay3firstname = sm.createinitialshex(SBay3firstname)
SBay3secondname = sm.createinitialshex(SBay3secondname)
SBay3thirdname = sm.createinitialshex(SBay3thirdname)
DL3firsttime, DL3secondtime, DL3thirdtime = sm.extracttimes_mariner(DL3data)
DL3firstname, DL3secondname, DL3thirdname = sm.extractnames(DL3data)
DL3firstname = sm.createinitialshex(DL3firstname)
DL3secondname = sm.createinitialshex(DL3secondname)
DL3thirdname = sm.createinitialshex(DL3thirdname)
MF3firsttime, MF3secondtime, MF3thirdtime = sm.extracttimes_jeter(MF3data)
MF3firstname, MF3secondname, MF3thirdname = sm.extractnames(MF3data)
MF3firstname = sm.createinitialshex(MF3firstname)
MF3secondname = sm.createinitialshex(MF3secondname)
MF3thirdname = sm.createinitialshex(MF3thirdname)
PB3firsttime, PB3secondtime, PB3thirdtime = sm.extracttimes_jeter(PB3data)
PB3firstname, PB3secondname, PB3thirdname = sm.extractnames(PB3data)
PB3firstname = sm.createinitialshex(PB3firstname)
PB3secondname = sm.createinitialshex(PB3secondname)
PB3thirdname = sm.createinitialshex(PB3thirdname)
TC3firsttime, TC3secondtime, TC3thirdtime = sm.extracttimes_mariner(TC3data)
TC3firstname, TC3secondname, TC3thirdname = sm.extractnames(TC3data)
TC3firstname = sm.createinitialshex(TC3firstname)
TC3secondname = sm.createinitialshex(TC3secondname)
TC3thirdname = sm.createinitialshex(TC3thirdname)
GC3firsttime, GC3secondtime, GC3thirdtime = sm.extracttimes_mariner(GC3data)
GC3firstname, GC3secondname, GC3thirdname = sm.extractnames(GC3data)
GC3firstname = sm.createinitialshex(GC3firstname)
GC3secondname = sm.createinitialshex(GC3secondname)
GC3thirdname = sm.createinitialshex(GC3thirdname)
SI3firsttime, SI3secondtime, SI3thirdtime = sm.extracttimes_mariner(SI3data)
SI3firstname, SI3secondname, SI3thirdname = sm.extractnames(SI3data)
SI3firstname = sm.createinitialshex(SI3firstname)
SI3secondname = sm.createinitialshex(SI3secondname)
SI3thirdname = sm.createinitialshex(SI3thirdname)

# Isolate 1 Lap times and names into individual variables for each level
SB1time = sm.extracttime_mariner(SB1data)
SB1name = SB1data.Player[0]
SB1name = sm.createinitialshex(SB1name)
SBay1time = sm.extracttime_mariner(SBay1data)
SBay1name = SBay1data.Player[0]
SBay1name = sm.createinitialshex(SBay1name)
DL1time = sm.extracttime_mariner(DL1data)
DL1name = DL1data.Player[0]
DL1name = sm.createinitialshex(DL1name)
MF1time = sm.extracttime_jeter(MF1data)
MF1name = MF1data.Player[0]
MF1name = sm.createinitialshex(MF1name)
PB1time = sm.extracttime_jeter(PB1data)
PB1name = PB1data.Player[0]
PB1name = sm.createinitialshex(PB1name)
TC1time = sm.extracttime_mariner(TC1data)
TC1name = TC1data.Player[0]
TC1name = sm.createinitialshex(TC1name)
GC1time = sm.extracttime_mariner(GC1data)
GC1name = GC1data.Player[0]
GC1name = sm.createinitialshex(GC1name)
SI1time = sm.extracttime_mariner(SI1data)
SI1name = SI1data.Player[0]
SI1name = sm.createinitialshex(SI1name)

# Isolate Reverse time and name into individual variables for each level
SBRtime = sm.extracttime_mariner(SBRdata)
SBRname = SBRdata.Player[0]
SBRname = sm.createinitialshex(SBRname)
SBayRtime = sm.extracttime_mariner(SBayRdata)
SBayRname = SBayRdata.Player[0]
SBayRname = sm.createinitialshex(SBayRname)
DLRtime = sm.extracttime_mariner(DLRdata)
DLRname = DLRdata.Player[0]
DLRname = sm.createinitialshex(DLRname)
MFRtime = sm.extracttime_hayami(MFRdata)
MFRname = MFRdata.Player[0]
MFRname = sm.createinitialshex(MFRname)
PBRtime = sm.extracttime_jeter(PBRdata)
PBRname = PBRdata.Player[0]
PBRname = sm.createinitialshex(PBRname)
TCRtime = sm.extracttime_mariner(TCRdata)
TCRname = TCRdata.Player[0]
TCRname = sm.createinitialshex(TCRname)
GCRtime = sm.extracttime_mariner(GCRdata)
GCRname = GCRdata.Player[0]
GCRname = sm.createinitialshex(GCRname)
SIRtime = sm.extracttime_mariner(SIRdata)
SIRname = SIRdata.Player[0]
SIRname = sm.createinitialshex(SIRname)


#######################
### Build Save File ###
#######################

######################
### Write Settings ###
######################

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

# Write R.Hayami Name & 00 to signify end of name
sm.writetooffset(bytes.fromhex('522E484159414D4900FF'), 0x10)

# Write D.Mariner Name & 00 to signify end of name
sm.writetooffset(bytes.fromhex('442E4D4152494E455200'), 0x1A)

# Write A.Stewart Name & 00 to signify end of name
sm.writetooffset(bytes.fromhex('412E5354455741525400'), 0x24)

# Write M.Jeter Name & 00 to signify end of name
sm.writetooffset(bytes.fromhex('4D2E4A4554455200FFFF'), 0x2E)

# Write Hayami Custom Craft Settings
sm.writetooffset(bytes.fromhex('050806'), 0x38)

# Write Mariner Custom Craft Settings
sm.writetooffset(bytes.fromhex('000B0B'), 0x3B)

# Write Stewart Custom Craft Settings
sm.writetooffset(bytes.fromhex('050505'), 0x3E)

# Write Jeter Custom Craft Settings
sm.writetooffset(bytes.fromhex('080B05'), 0x41)

# Write Default Craft Settings
sm.writetooffset(bytes.fromhex('050505050505050505050505'), 0x44)

# Write Normal Conditions
sm.writetooffset(bytes.fromhex('000503'), 0x50)

# Write Hard Conditions
sm.writetooffset(bytes.fromhex('000503'), 0x53)

# Write Expert Conditions
sm.writetooffset(bytes.fromhex('000503'), 0x56)

# Write FF Spaces for end of settings
sm.writetooffset(bytes.fromhex('FFFFFFFFFFFFFF'), 0x59)


#####################################
### Write Record Times & Initials ###
#####################################

############## SUNNY BEACH ##############

# Write Sunny Beach 3L World Record Time
sm.writetooffset(bytes.fromhex(SB3firsttime), 0x60)

# Write Sunny Beach 3L World Record Initials
sm.writetooffset(bytes.fromhex(SB3firstname), 0x63)

# Write Sunny Beach 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x65)

# Write Sunny Beach 3L Second Place Time
sm.writetooffset(bytes.fromhex(SB3secondtime), 0x66)

# Write Sunny Beach 3L Second Place Initials
sm.writetooffset(bytes.fromhex(SB3secondname), 0x69)

# Write Sunny Beach 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x6B)

# Write Sunny Beach 3L Third Place Time
sm.writetooffset(bytes.fromhex(SB3thirdtime), 0x6C)

# Write Sunny Beach 3L Third Place Initials
sm.writetooffset(bytes.fromhex(SB3thirdname), 0x6F)

# Write Sunny Beach 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x71)

# Write Sunny Beach 1L World Record Time
sm.writetooffset(bytes.fromhex(SB1time), 0x72)

# Write Sunny Beach 1L World Record Initials
sm.writetooffset(bytes.fromhex(SB3firstname), 0x75)

# Write Sunny Beach 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x77)

############## SUNSET BAY ##############

# Write Sunset Bay 3L World Record Time
sm.writetooffset(bytes.fromhex(SBay3firsttime), 0x78)

# Write Sunset Bay 3L World Record Initials
sm.writetooffset(bytes.fromhex(SBay3firstname), 0x7B)

# Write Sunset Bay 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x7D)

# Write Sunset Bay 3L Second Place Time
sm.writetooffset(bytes.fromhex(SBay3secondtime), 0x7E)

# Write Sunset Bay 3L Second Place Initials
sm.writetooffset(bytes.fromhex(SBay3secondname), 0x81)

# Write Sunset Bay 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x83)

# Write Sunset Bay 3L Third Place Time
sm.writetooffset(bytes.fromhex(SBay3thirdtime), 0x84)

# Write Sunset Bay 3L Third Place Initials
sm.writetooffset(bytes.fromhex(SBay3thirdname), 0x87)

# Write Sunset Bay 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x89)

# Write Sunset Bay 1L World Record Time
sm.writetooffset(bytes.fromhex(SBay1time), 0x8A)

# Write Sunset Bay 1L World Record Initials
sm.writetooffset(bytes.fromhex(SBay1name), 0x8D)

# Write Sunset Bay 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x8F)

############## MARINE FORTRESS ##############

# Write Marine Fortress 3L World Record Time
sm.writetooffset(bytes.fromhex(MF3firsttime), 0x90)

# Write Marine Fortress 3L World Record Initials
sm.writetooffset(bytes.fromhex(MF3firstname), 0x93)

# Write Marine Fortress 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('01'), 0x95)

# Write Marine Fortress 3L Second Place Time
sm.writetooffset(bytes.fromhex(MF3secondtime), 0x96)

# Write Marine Fortress 3L Second Place Initials
sm.writetooffset(bytes.fromhex(MF3secondname), 0x99)

# Write Marine Fortress 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('01'), 0x9B)

# Write Marine Fortress 3L Third Place Time
sm.writetooffset(bytes.fromhex(MF3thirdtime), 0x9C)

# Write Marine Fortress 3L Third Place Initials
sm.writetooffset(bytes.fromhex(MF3thirdname), 0x9F)

# Write Marine Fortress 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xA1)

# Write Marine Fortress 1L World Record Time
sm.writetooffset(bytes.fromhex(MF1time), 0xA2)

# Write Marine Fortress 1L World Record Initials
sm.writetooffset(bytes.fromhex(MF1name), 0xA5)

# Write Marine Fortress 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xA7)

############## DRAKE LAKE ##############

# Write Drake Lake 3L World Record Time
sm.writetooffset(bytes.fromhex(DL3firsttime), 0xA8)

# Write Drake Lake 3L World Record Initials
sm.writetooffset(bytes.fromhex(DL3firstname), 0xAB)

# Write Drake Lake 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0xAD)

# Write Drake Lake 3L Second Place Time
sm.writetooffset(bytes.fromhex(DL3secondtime), 0xAE)

# Write Drake Lake 3L Second Place Initials
sm.writetooffset(bytes.fromhex(DL3secondname), 0xB1)

# Write Drake Lake 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0xB3)

# Write Drake Lake 3L Third Place Time
sm.writetooffset(bytes.fromhex(DL3thirdtime), 0xB4)

# Write Drake Lake 3L Third Place Initials
sm.writetooffset(bytes.fromhex(DL3thirdname), 0xB7)

# Write Drake Lake 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0xB9)

# Write Drake Lake 1L World Record Time
sm.writetooffset(bytes.fromhex(DL1time), 0xBA)

# Write Drake Lake 1L World Record Initials
sm.writetooffset(bytes.fromhex(DL1name), 0xBD)

# Write Drake Lake 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0xBF)

############## PORT BLUE ##############

# Write Port Blue 3L World Record Time
sm.writetooffset(bytes.fromhex(PB3firsttime), 0xC0)

# Write Port Blue 3L World Record Initials
sm.writetooffset(bytes.fromhex(PB3firstname), 0xC3)

# Write Port Blue 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xC5)

# Write Port Blue 3L Second Place Time
sm.writetooffset(bytes.fromhex(PB3secondtime), 0xC6)

# Write Port Blue 3L Second Place Initials
sm.writetooffset(bytes.fromhex(PB3secondname), 0xC9)

# Write Port Blue 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xCB)

# Write Port Blue 3L Third Place Time
sm.writetooffset(bytes.fromhex(PB3thirdtime), 0xCC)

# Write Port Blue 3L Third Place Initials
sm.writetooffset(bytes.fromhex(PB3thirdname), 0xCF)

# Write Port Blue 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xD1)

# Write Port Blue 1L World Record Time
sm.writetooffset(bytes.fromhex(PB1time), 0xD2)

# Write Port Blue 1L World Record Initials
sm.writetooffset(bytes.fromhex(PB1name), 0xD5)

# Write Port Blue 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xD7)

############## TWILIGHT CITY ##############

# Write Twilight City 3L World Record Time
sm.writetooffset(bytes.fromhex(TC3firsttime), 0xD8)

# Write Twilight City 3L World Record Initials
sm.writetooffset(bytes.fromhex(TC3firstname), 0xDB)

# Write Twilight City 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xDD)

# Write Twilight City 3L Second Place Time
sm.writetooffset(bytes.fromhex(TC3secondtime), 0xDE)

# Write Twilight City 3L Second Place Initials
sm.writetooffset(bytes.fromhex(TC3secondname), 0xE1)

# Write Twilight City 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xE3)

# Write Twilight City 3L Third Place Time
sm.writetooffset(bytes.fromhex(TC3thirdtime), 0xE4)

# Write Twilight City 3L Third Place Initials
sm.writetooffset(bytes.fromhex(TC3thirdname), 0xE7)

# Write Twilight City 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xE9)

# Write Twilight City 1L World Record Time
sm.writetooffset(bytes.fromhex(TC1time), 0xEA)

# Write Twilight City 1L World Record Initials
sm.writetooffset(bytes.fromhex(TC1name), 0xED)

# Write Twilight City 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('01'), 0xEF)

############## SOUTHERN ISLAND ##############

# Write Southern Island 3L World Record Time
sm.writetooffset(bytes.fromhex(SI3firsttime), 0xF0)

# Write Southern Island 3L World Record Initials
sm.writetooffset(bytes.fromhex(SI3firstname), 0xF3)

# Write Southern Island 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0xF5)

# Write Southern Island 3L Second Place Time
sm.writetooffset(bytes.fromhex(SI3secondtime), 0xF6)

# Write Southern Island 3L Second Place Initials
sm.writetooffset(bytes.fromhex(SI3secondname), 0xF9)

# Write Southern Island 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0xFB)

# Write Southern Island 3L Third Place Time
sm.writetooffset(bytes.fromhex(SI3thirdtime), 0xFC)

# Write Southern Island 3L Third Place Initials
sm.writetooffset(bytes.fromhex(SI3thirdname), 0xFF)

# Write Southern Island 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x101)

# Write Southern Island 1L World Record Time
sm.writetooffset(bytes.fromhex(SI1time), 0x102)

# Write Southern Island 1L World Record Initials
sm.writetooffset(bytes.fromhex(SI1name), 0x105)

# Write Southern Island 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('00'), 0x107)

############## GLACIER COAST ##############

# Write Glacier Coast 3L World Record Time
sm.writetooffset(bytes.fromhex(GC3firsttime), 0x108)

# Write Glacier Coast 3L World Record Initials
sm.writetooffset(bytes.fromhex(GC3firstname), 0x10B)

# Write Glacier Coast 3L World Record Difficulty
sm.writetooffset(bytes.fromhex('02'), 0x10D)

# Write Glacier Coast 3L Second Place Time
sm.writetooffset(bytes.fromhex(GC3secondtime), 0x10E)

# Write Glacier Coast 3L Second Place Initials
sm.writetooffset(bytes.fromhex(GC3secondname), 0x111)

# Write Glacier Coast 3L Second Place Difficulty
sm.writetooffset(bytes.fromhex('02'), 0x113)

# Write Glacier Coast 3L Third Place Time
sm.writetooffset(bytes.fromhex(GC3thirdtime), 0x114)

# Write Glacier Coast 3L Third Place Initials
sm.writetooffset(bytes.fromhex(GC3thirdname), 0x117)

# Write Glacier Coast 3L Third Place Difficulty
sm.writetooffset(bytes.fromhex('02'), 0x119)

# Write Glacier Coast 1L World Record Time
sm.writetooffset(bytes.fromhex(GC1time), 0x11A)

# Write Glacier Coast 1L World Record Initials
sm.writetooffset(bytes.fromhex(GC1name), 0x11D)

# Write Glacier Coast 1L World Record Difficulty
sm.writetooffset(bytes.fromhex('02'), 0x11F)


##############################
### Write Scores & Initials###
##############################

# Write Dolphin Park first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x120)

# Write Dolphin Park second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x125)

# Write Dolphin Park third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x12A)

# Write Sunny Beach first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x12F)

# Write Sunny Beach second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x134)

# Write Sunny Beach third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x1249)

# Write Sunset Bay first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x13E)

# Write Sunset Bay second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x143)

# Write Sunset Bay third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x148)

# Write Marine Fortress first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x14D)

# Write Marine Fortress second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x152)

# Write Marine Fortress third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x157)

# Write Drake Lake first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x15C)

# Write Drake Lake second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x161)

# Write Drake Lake third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x166)

# Write Port Blue first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x16B)

# Write Port Blue second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x170)

# Write Port Blue third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x175)

# Write Twilight City first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x17A)

# Write Twilight City second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x17F)

# Write Twilight City third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x184)

# Write Southern Island first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x189)

# Write Southern Island second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x18E)

# Write Southern Island third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x193)

# Write Glacier Coast first place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x198)

# Write Glacier Coast second place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x190)

# Write Glacier Coast third place score & initials
sm.writetooffset(bytes.fromhex('0000000000'), 0x1A2)


#########################
### Write Split Times ###
#########################

# Write FF Space before splits
sm.writetooffset(bytes.fromhex('FF'), 0x1A7)

# Write Sunny Beach Split 1
sm.writetooffset(bytes.fromhex(splits.SB_split1), 0x1A8)

# Write Sunny Beach Split 2
sm.writetooffset(bytes.fromhex(splits.SB_split2), 0x1AB)

# Write Sunset Bay Split 1
sm.writetooffset(bytes.fromhex(splits.SBay_split1), 0x1AE)

# Write Sunset Bay Split 2
sm.writetooffset(bytes.fromhex(splits.SBay_split2), 0x1B1)

# Write Marine Fortress Split 1
sm.writetooffset(bytes.fromhex(splits.MF_split1), 0x1B4)

# Write Marine Fortress Split 2
sm.writetooffset(bytes.fromhex(splits.MF_split2), 0x1B7)

# Write Drake Lake Split 1
sm.writetooffset(bytes.fromhex(splits.DL_split1), 0x1BA)

# Write Drake Lake Split 2
sm.writetooffset(bytes.fromhex(splits.DL_split2), 0x1BD)

# Write Port Blue Split 1
sm.writetooffset(bytes.fromhex(splits.PB_split1), 0x1C0)

# Write Port Blue Split 2
sm.writetooffset(bytes.fromhex(splits.PB_split2), 0x1C3)

# Write Twilight City Split 1
sm.writetooffset(bytes.fromhex(splits.TC_split1), 0x1C6)

# Write Twilight City Split 2
sm.writetooffset(bytes.fromhex(splits.TC_split2), 0x1C9)

# Write Southern Island Split 1
sm.writetooffset(bytes.fromhex(splits.SI_split1), 0x1CC)

# Write Southern Island Split 2
sm.writetooffset(bytes.fromhex(splits.SI_split2), 0x1CF)

# Write Glacier Coast Split 1
sm.writetooffset(bytes.fromhex(splits.GC_split1), 0x1D2)

# Write Glacier Coast Split 2
sm.writetooffset(bytes.fromhex(splits.GC_split2), 0x1D5)


#############################################
### Write Reverse Record Times & Initials ###
#############################################

# Write Sunny Beach Reverse World Record time
sm.writetooffset(bytes.fromhex(SBRtime), 0x1D8)

# Write Sunny Beach Reverse World Record initials
sm.writetooffset(bytes.fromhex(SBRname), 0x1DB)

# Write Sunset Bay Reverse World Record time
sm.writetooffset(bytes.fromhex(SBayRtime), 0x1DD)

# Write Sunset Bay Reverse World Record initials
sm.writetooffset(bytes.fromhex(SBayRname), 0x1E0)

# Write Marine Fortress Reverse World Record time
sm.writetooffset(bytes.fromhex(MFRtime), 0x1E2)

# Write Marine Fortress Reverse World Record initials
sm.writetooffset(bytes.fromhex(MFRname), 0x1E5)

# Write Drake Lake Reverse World Record time
sm.writetooffset(bytes.fromhex(DLRtime), 0x1E7)

# Write Drake Lake Reverse World Record initials
sm.writetooffset(bytes.fromhex(DLRname), 0x1EA)

# Write Port Blue Reverse World Record time
sm.writetooffset(bytes.fromhex(PBRtime), 0x1EC)

# Write Port Blue Reverse World Record initials
sm.writetooffset(bytes.fromhex(PBRname), 0x1EF)

# Write Twilight City Reverse World Record time
sm.writetooffset(bytes.fromhex(TCRtime), 0x1F1)

# Write Twilight City Reverse World Record initials
sm.writetooffset(bytes.fromhex(TCRname), 0x1F4)

# Write Southern Island Reverse World Record time
sm.writetooffset(bytes.fromhex(SIRtime), 0x1F6)

# Write Southern Island Reverse World Record initials
sm.writetooffset(bytes.fromhex(SIRname), 0x1F9)

# Write Glacier Coast Reverse World Record time
sm.writetooffset(bytes.fromhex(GCRtime), 0x1FB)

# Write Glacier Coast Reverse World Record initials
sm.writetooffset(bytes.fromhex(GCRname), 0x1FE)


######################
### Write Checksum ###
######################

checksum = sm.calculatechecksum()
sm.writetooffset(bytes.fromhex(checksum), 0x2)