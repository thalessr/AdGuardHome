# Mikrotik AdguardHome

Mikrotik RouterOS v6

## Usage

### Download the lists


```sh
/system script add name="downloadAdGuardHomeStalkerwareList" owner="Mikrotik" source={
	/tool fetch url="https://raw.githubusercontent.com/thalessr/AdGuardHome/main/dist/stalkerware.rsc" mode=https;
	:delay 2;
	/ip firewall address-list remove [find where comment="AdGuardHome-Stalkerware"];
	:delay 2;
	/import file-name=stalkerware.rsc;
	:delay 2;
	/file remove stalkerware.rsc;
}
```
And
```sh

/system script add name="downloadAdGuardHomeADblockerList" owner="Mikrotik" source={
	/tool fetch url="https://raw.githubusercontent.com/thalessr/AdGuardHome/main/dist/adblock.rsc" mode=https;
	:delay 2;
	/ip firewall address-list remove [find where comment="AdGuardHome-ADblocker"];
	:delay 2;
	/import file-name=adblock.rsc;
	:delay 2;
	/file remove adblock.rsc;
}
```

## Drop the connection via Firewall RAW

```sh
/ip firewall raw
add action=drop chain=prerouting src-address-list=stalkerware comment="AdGuardHome Stalkerware"
add action=drop chain=prerouting src-address-list=adblocker comment="AdGuardHome Adblocker"
```

## Add a scheduler to keep the lists up to date

```sh
/system scheduler add comment="AdGuardHome" interval=1d name="StalkerwareListUpdate" on-event=downloadAdGuardHomeStalkerwareList start-date=Mar/22/2024 start-time=01:00:00
```
and

```sh
/system scheduler add comment="AdGuardHome" interval=1d name="ADblockerListUpdate" on-event=downloadAdGuardHomeADblockerList start-date=Mar/22/2024 start-time=01:05:00
```
