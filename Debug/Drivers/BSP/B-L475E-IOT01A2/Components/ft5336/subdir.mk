################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (13.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.c 

OBJS += \
./Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.o 

C_DEPS += \
./Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/%.o Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/%.su Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/%.cyclo: ../Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/%.c Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L475xx -c -I../Core/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -I../BlueNRG_MS/App -I../BlueNRG_MS/Target -I../Drivers/BSP/B-L475E-IOT01A2 -I../Middlewares/ST/BlueNRG-MS/utils -I../Middlewares/ST/BlueNRG-MS/includes -I../Middlewares/ST/BlueNRG-MS/hci/hci_tl_patterns/Basic -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP-2f-B-2d-L475E-2d-IOT01A2-2f-Components-2f-ft5336

clean-Drivers-2f-BSP-2f-B-2d-L475E-2d-IOT01A2-2f-Components-2f-ft5336:
	-$(RM) ./Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.cyclo ./Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.d ./Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.o ./Drivers/BSP/B-L475E-IOT01A2/Components/ft5336/ft5336.su

.PHONY: clean-Drivers-2f-BSP-2f-B-2d-L475E-2d-IOT01A2-2f-Components-2f-ft5336

