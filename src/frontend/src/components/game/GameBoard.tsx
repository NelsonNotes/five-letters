import React, { useEffect } from 'react'

import './Game.css'

import { useAppDispatch } from '../../hooks/app'
import { TAttemptResponse } from '../../types/attempt'
import { AttemptLetterStatus } from '../../types/attempt'

interface Props {
	userAttempts: TAttemptResponse[]
}

export const GameBoard: React.FC<Props> = (props: Props) => {
	const { userAttempts } = props
	const dispatch = useAppDispatch()

	const getColorByStatus = (status: AttemptLetterStatus) => {
		switch (status) {
			case AttemptLetterStatus.Correct:
				return 'green'
			case AttemptLetterStatus.Included:
				return 'orange'
			case AttemptLetterStatus.Incorrect:
				return 'gray'
		}
	}

	return (
		<div>
			{userAttempts.map((attempt, idx) => {
				const attemptByLetters = attempt.attempt.split('')

				return (
					<div
						key={idx}
						style={{ display: 'flex', flexFlow: 'row', marginBottom: '60px' }}
					>
						{attemptByLetters.map((letter, idx) => {
							return (
								<div
									key={idx}
									style={{
										fontSize: '72px',
										color: getColorByStatus(attempt.letters_status[idx]),
									}}
								>
									{letter}
								</div>
							)
						})}
					</div>
				)
			})}
		</div>
	)
}
